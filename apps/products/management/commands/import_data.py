import csv
from datetime import datetime

from django.core.management import BaseCommand
from apps.products.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("import_data.csv", "r") as file:
            data_all = list(csv.DictReader(file, delimiter=";"))

        for category in data_all:
            Category.objects.create(name=category["category"])
