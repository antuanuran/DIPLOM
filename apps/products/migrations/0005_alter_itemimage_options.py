# Generated by Django 4.2.5 on 2023-12-24 06:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_vendor_options_itemimage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="itemimage",
            options={
                "verbose_name": "Фото товара",
                "verbose_name_plural": "Фото товара",
            },
        ),
    ]