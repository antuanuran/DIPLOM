# Generated by Django 4.2.5 on 2023-11-13 03:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_category_is_active_item_is_active_product_is_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "1. Категория", "verbose_name_plural": "1. Категории"},
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "3. Товар", "verbose_name_plural": "3. Товары"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "2. Продукт", "verbose_name_plural": "2. Продукты"},
        ),
        migrations.AlterModelOptions(
            name="vendor",
            options={"verbose_name": "Поставщик / Вендор", "verbose_name_plural": "Поставщики / Вендоры"},
        ),
    ]
