import csv
import yaml
from yaml import Loader
from rest_framework.exceptions import ValidationError


import os


from apps.products.models import (
    Category,
    Product,
    Vendor,
    Item,
    Attribute,
    ItemParameter,
)


def load_data_from_yml(data_stream):
    return yaml.load(data_stream, Loader=Loader)


def load_data_from_csv(data_stream):
    return csv.DictReader(data_stream, delimiter=",")


SUPPORTED_DATA_FORMATS = {
    "yml": load_data_from_yml,
    "yaml": load_data_from_yml,
    "csv": load_data_from_csv,
}


def load_data_yml(data, owner_id):
    vendor, _ = Vendor.objects.get_or_create(name=data["shop"], defaults={"owner_id": owner_id})

    new_category_id = {}
    for entity in data.get("categories", []):
        db_cat, _ = Category.objects.get_or_create(name=entity["name"])
        new_category_id[entity["id"]] = db_cat.id

    for entity in data.get("goods", []):
        product, _ = Product.objects.get_or_create(vendor=vendor, category_id=new_category_id[entity["category"]], name=entity["name"])

        item = Item.objects.filter(upc=entity["id"], product__vendor_id=vendor.id).first()
        if item:
            item.product = product
            item.price = entity["price"]
            item.count = entity["quantity"]
            item.save(update_fields=["product", "price", "count"])

        else:
            item = Item.objects.create(
                product=product,
                price=entity["price"],
                count=entity["quantity"],

                upc=entity["id"],
            )

        ItemParameter.objects.filter(item_id=item.id).delete()

        for key, value in entity['parameters'].items():
            if key:
                attribute_temp, _ = Attribute.objects.get_or_create(name=key, product_id=product.id)

                if value:
                    item_temp, _ = ItemParameter.objects.get_or_create(item_id=item.id, value=value, attribute_id=attribute_temp.id)
                else:
                    item_temp, _ = ItemParameter.objects.get_or_create(item_id=item.id, value="", attribute_id=attribute_temp.id)


def load_data_csv(data, owner_id):
    for entity in data:
        if entity["vendor_name"] and entity["product_name"] and entity["product_id"] and entity["price"] and entity["quantity"] and entity["category_id"] and entity["category_name"]:
            continue
        else:
            raise ValidationError(f"Отсутствуют значение одного из полей: vendor_name / product_name / price / quantity / category_id / category_name", code="no-value-in-fields")

    for entity in data:
        vendor, _ = Vendor.objects.get_or_create(name=entity.get("vendor_name", []), owner_id=owner_id)

        db_cat, _ = Category.objects.get_or_create(name=entity.get("category_name", []))
        new_category_id = db_cat.id

        product, _ = Product.objects.get_or_create(vendor_id=vendor.id, category_id=new_category_id, name=entity["product_name"])

        item = Item.objects.filter(upc=entity["product_id"], product__vendor_id=vendor.id).first()

        if item:
            item.price = entity["price"]
            item.count = entity["quantity"]
            item.product = product

            item.save(update_fields=["product", "price", "count"])

        else:
            item = Item.objects.create(
                price=entity["price"],
                count=entity["quantity"],
                product_id=product.id,
                upc=entity["product_id"],
            )

        all_keys = ["vendor_name", "product_name", "product_id", "price", "quantity", "category_id", "category_name"]

        ItemParameter.objects.filter(item_id=item.id).delete()

        for key, value in entity.items():
            if key not in all_keys:
                if value:
                    attribute_temp, _ = Attribute.objects.get_or_create(name=key, product_id=product.id)
                    item_temp, _ = ItemParameter.objects.get_or_create(item_id=item.id, value=value, attribute_id=attribute_temp.id)


def import_data(data_stream, data_format: str, owner_id):
    if data_format not in SUPPORTED_DATA_FORMATS:
        raise NotImplementedError(
            f"{data_format} not supported. Available only: {SUPPORTED_DATA_FORMATS.keys()}"
        )
    elif data_format == "csv":
        data = SUPPORTED_DATA_FORMATS[data_format](data_stream)
        load_data_csv(data, owner_id)
    else:
        data = SUPPORTED_DATA_FORMATS[data_format](data_stream)
        load_data_yml(data, owner_id)


def convert_to_csv(data):
    my_file = open("data_all/temp.txt", "w+")
    my_file.write(data)
    my_file.close()

    with open("data_all/temp.txt", "r") as in_file:
        items = []
        for line in in_file:
            str_file = line.strip()
            items.append(str_file.split(","))
        with open("data_all/temp.csv", "w") as out_file:
            writer = csv.writer(out_file)
            writer.writerows(items)

    with open("data_all/temp.csv", "r", encoding="utf-8") as fd:
        data_stream_csv = list(csv.DictReader(fd))

    os.remove("data_all/temp.csv")
    os.remove("data_all/temp.txt")

    return data_stream_csv


def import_http_csv(data_stream, owner_id):
    data_all = convert_to_csv(data_stream)
    load_data_csv(data_all, owner_id)
