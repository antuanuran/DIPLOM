# Generated by Django 4.2.5 on 2023-12-28 07:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_alter_itemimage_options"),
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
