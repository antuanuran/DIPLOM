from django.core.validators import MinValueValidator
from django.db import models

from apps.users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attributes")

    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'

    def __str__(self):
        return self.name


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    price = models.IntegerField(validators=[MinValueValidator(1)])
    count = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    # def __str__(self):
    #     return self.product


class ItemParameter(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="parameters")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="parameters")
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Конкретный товар'
        verbose_name_plural = 'Конкретные товары'

    def __str__(self):
        return self.value


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vendors")

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
