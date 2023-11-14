# Generated by Django 4.2.5 on 2023-11-03 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Покупка", "verbose_name_plural": "Покупки"},
        ),
        migrations.AlterModelOptions(
            name="orderrow",
            options={"verbose_name": "Покупка", "verbose_name_plural": "Покупки"},
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]