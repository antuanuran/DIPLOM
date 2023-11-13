from django.contrib import admin
from apps.basket.models import BasketRow, Basket
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class BasketRowInLineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            if form.cleaned_data["DELETE"]:
                continue
            if form.cleaned_data["qty"] > form.cleaned_data["item"].count:
                raise ValidationError(
                    f"Max Limit count  [{form.cleaned_data['item'].product.name}] - {form.cleaned_data['item'].count}"
                )


class BasketRowInLine(admin.TabularInline):
    model = BasketRow
    extra = 0
    readonly_fields = ["sum_basket_row"]
    formset = BasketRowInLineFormset


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "sum_basket"]
    readonly_fields = ["sum_basket"]
    search_fields = ["user__email"]

    inlines = [BasketRowInLine]
