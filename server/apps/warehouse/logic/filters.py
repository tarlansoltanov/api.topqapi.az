from django_filters import rest_framework as filters

from server.apps.warehouse.models import WarehouseEntry, WarehouseItem


class WarehouseItemFilter(filters.FilterSet):
    """FilterSet class for WarehouseItem model."""

    product = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    category = filters.CharFilter(field_name="product__category__name", lookup_expr="icontains")
    supplier = filters.CharFilter(field_name="entry__supplier__name", lookup_expr="icontains")

    class Meta:
        model = WarehouseItem
        fields = (
            "product",
            "category",
            "supplier",
        )


class WarehouseEntryFilter(filters.FilterSet):
    """FilterSet class for WarehouseEntry model."""

    supplier = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = WarehouseEntry
        fields = (
            "supplier",
            "date_start",
            "date_end",
        )
