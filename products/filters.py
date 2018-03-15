import django_filters
from django import forms

from products.models import Material, Colour, Stock, Size


class ProductFilter(django_filters.FilterSet):
    product__product_material = django_filters.ModelMultipleChoiceFilter(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    product__product_color = django_filters.ModelMultipleChoiceFilter(
        queryset=Colour.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    size = django_filters.ModelMultipleChoiceFilter(
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Stock
        fields = ['product__product_color', 'product__product_material', 'size']
