from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models

from apps.users.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vendors")

    class Meta:
        verbose_name = "1. Поставщик"
        verbose_name_plural = "1. Поставщики"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # products

    class Meta:
        verbose_name = "2. Категория"
        verbose_name_plural = "2. Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="products"
    )
    # attributes
    # items

    class Meta:
        verbose_name = "3. Продукт"
        verbose_name_plural = "3. Продукты"

    def __str__(self):
        return f"{self.name}"


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="attributes"
    )
    # parameters - ссылка на конкретный параметр

    class Meta:
        verbose_name = "Атрибут"
        verbose_name_plural = "Атрибуты"

    def __str__(self):
        return f"{self.name}: [{self.product.name}]"


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    price = models.IntegerField(validators=[MinValueValidator(1)])
    count = models.PositiveIntegerField()
    upc = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    # parameters
    # basket_rows (Model from basket App)
    # baskets     (Model from basket App)

    # Проверка на уникальность upc+vendor (при альтернативной загрузке - админка либо реквест)
    # ****************************************************************************************
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        if not self.upc:
            return
        if (
            Item.objects.filter(
                product__vendor__id=self.product.vendor_id, upc=self.upc
            )
            .exclude(id=self.id)
            .exists()
        ):
            raise ValidationError({"non unique id (goods)"}, code="non-unique-upc")

    class Meta:
        verbose_name = "4. Товар"
        verbose_name_plural = "4. Товары"

    # ****************************************************************************************

    def __str__(self):
        return f"{self.product} [{self.price} руб. / {self.count} шт.]"


class ItemParameter(models.Model):
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="parameters"
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="parameters")
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Конкретный параметр"
        verbose_name_plural = "Конкретные параметры"

    def __str__(self):
        return self.value
