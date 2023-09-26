import csv

import yaml
from yaml import Loader

from apps.products.models import Category


def load_data_from_yml(data_stream):
    return yaml.load(data_stream, Loader=Loader)


def load_data_from_csv(data_stream):
    return csv.DictReader(data_stream, delimiter=";")


SUPPORTED_DATA_FORMATS = {
    "yml": load_data_from_yml,
    "yaml": load_data_from_yml,
    "csv": load_data_from_csv,
}


def load_data_yml(data):
    all = data.get("categories")
    for i in all:
        Category.objects.bulk_create([Category(name=i.get("name")) for i in all], ignore_conflicts=True)


def load_data_csv(data):
    Category.objects.bulk_create([Category(name=category["category"]) for category in data], ignore_conflicts=True)


def import_data(data_stream, data_format: str):
    if data_format not in SUPPORTED_DATA_FORMATS:
        raise NotImplementedError(f"{data_format} not supported. Available only: {SUPPORTED_DATA_FORMATS.keys()}")
    elif data_format == "csv":
        data = SUPPORTED_DATA_FORMATS[data_format](data_stream)
        load_data_csv(data)
    else:
        data = SUPPORTED_DATA_FORMATS[data_format](data_stream)
        load_data_yml(data)
