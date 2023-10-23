import csv
import yaml
from yaml import Loader


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
    vendor, _ = Vendor.objects.get_or_create(
        name=data["shop"], defaults={"owner_id": owner_id}
    )

    category_mapper = {}
    for entity in data.get("categories", []):
        db_cat, _ = Category.objects.get_or_create(name=entity["name"])
        category_mapper[entity["id"]] = db_cat.id

    for entity in data.get("goods", []):
        product, _ = Product.objects.get_or_create(
            vendor=vendor,
            category_id=category_mapper[entity["category"]],
            name=entity["name"],
        )

        item = Item.objects.filter(upc=entity["id"], product__vendor=vendor).first()
        if item:
            item.product = product
            item.price = entity["price"]
            item.count = entity["quantity"]
            item.save(update_fields=["product", "price", "count"])

        else:
            item = Item.objects.create(
                price=entity["price"],
                count=entity["quantity"],
                upc=entity["id"],
                product=product,
            )

        desired_attributes = set(entity.get("parameters", {}).keys())
        for temp in desired_attributes:
            attr, _ = Attribute.objects.get_or_create(name=temp, product=product)

        item.parameters.all().delete()
        for key, value in entity.get("parameters", {}).items():
            ItemParameter.objects.create(
                value=value,
                item=item,
                attribute=Attribute.objects.get(name=key, product=product),
            )


def load_data_csv(data, owner_id):
    category_mapper = {}
    for entity in data:
        if entity["vendor_name"]:
            vendor, _ = Vendor.objects.get_or_create(
                name=entity["vendor_name"], defaults={"owner_id": owner_id}
            )

        if entity["category_name"]:
            db_cat, _ = Category.objects.get_or_create(name=entity["category_name"])
            category_mapper[entity["category_id"]] = db_cat.id

        if entity["product_name"]:
            product, _ = Product.objects.get_or_create(
                vendor=vendor,
                category_id=category_mapper[entity["category_product_id"]],
                name=entity["product_name"],
            )

        item = Item.objects.filter(
            upc=entity["product_id"], product__vendor=vendor
        ).first()
        if item:
            item.product = product
            item.price = entity["price"]
            item.count = entity["quantity"]
            item.save(update_fields=["product", "price", "count"])

        else:
            item = Item.objects.create(
                price=entity["price"],
                count=entity["quantity"],
                upc=entity["product_id"],
                product=product,
            )

        all_keys = [
            "vendor_name",
            "categories",
            "category_name",
            "category_id",
            "goods",
            "product_name",
            "product_id",
            "price",
            "quantity",
            "category_product_id",
            "parameters",
        ]
        for key, value in entity.items():
            if key not in all_keys:
                if value:
                    Attribute.objects.get_or_create(name=key, product=product)

        item.parameters.all().delete()

        for key, value in entity.items():
            if key not in all_keys:
                if value:
                    ItemParameter.objects.create(
                        value=value,
                        item=item,
                        attribute=Attribute.objects.get(name=key, product=product),
                    )


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
