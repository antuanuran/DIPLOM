from django.db import models

from apps.products.models import Item
from apps.users.models import User


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="baskets")
    items = models.ManyToManyField(Item, through="BasketRow", related_name="baskets", blank=True)
    # rows

    @property
    def sum_total_all_baskets(self):
        total = 0
        for row in self.rows.all():
            total += row.sum_current_basket
        return total

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return self.user.email


class BasketRow(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="rows")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="basket_rows")
    qty = models.PositiveIntegerField(default=1)

    @property
    def sum_current_basket(self):
        return self.qty * self.item.price

    class Meta:
        verbose_name = "Заказ в корзине"
        verbose_name_plural = "Заказы в корзине"

    def __str__(self):
        return f"{self.basket.user.email}  ->  [ТОВАР: {self.item}]"
