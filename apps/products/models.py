from django.core.validators import MinValueValidator
from django.db import models

from apps.users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attributes")


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attributes")
    price = models.IntegerField(validators=[MinValueValidator(1)])
    count = models.PositiveIntegerField()


class ItemParameter(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="parameters")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="parameters")
    value = models.CharField(max_length=100)


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vendors")
