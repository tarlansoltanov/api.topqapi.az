from django.db import models

from server.apps.core.models import TimeStampedModel
from server.apps.order.logic.constants import OrderStatus
from server.apps.order.logic.queryset import OrderItemQuerySet, OrderQuerySet
from server.apps.order.logic.utils import send_status_change_email


class Order(TimeStampedModel):
    """Model definition for Order."""

    branch = models.ForeignKey("branch.Branch", on_delete=models.CASCADE, related_name="orders")
    seller = models.ForeignKey("staff.Seller", on_delete=models.CASCADE, related_name="orders")

    customer = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    note = models.TextField(blank=True)

    payed = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    sale_date = models.DateField()
    seller_share = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    driver = models.ForeignKey(
        "staff.Driver",
        on_delete=models.CASCADE,
        related_name="orders",
        blank=True,
        null=True,
    )
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_date = models.DateField(blank=True, null=True)

    worker = models.ForeignKey(
        "staff.Worker",
        on_delete=models.CASCADE,
        related_name="orders",
        blank=True,
        null=True,
    )
    install_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    install_date = models.DateField(blank=True, null=True)

    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices, default=OrderStatus.DRAFT)

    objects = OrderQuerySet.as_manager()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of Order."""
        return f"Order: #{self.id}"

    def save(self, *args, **kwargs):
        """Send email notification to the seller when order status changes."""

        if self.pk:
            old_status = Order.objects.get(pk=self.pk).status
            if old_status != self.status and self.status > OrderStatus.REGISTERED:
                send_status_change_email(self, self.get_status_display())

        super().save(*args, **kwargs)


class OrderItem(TimeStampedModel):
    """Model definition for OrderItem."""

    order = models.ForeignKey("order.Order", on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="order_products")
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="order_products")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    size = models.CharField(max_length=255, blank=True)

    objects = OrderItemQuerySet.as_manager()

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of OrderItem."""
        return f"Order Item: {self.product.name}"


class OrderCartItem(TimeStampedModel):
    """Model definition for OrderCartItem."""

    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="order_cart")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="order_cart")
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.CASCADE, related_name="order_cart")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    size = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Order Cart Item"
        verbose_name_plural = "Order Cart Items"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of OrderCartItem."""
        return f"Order Cart Item: {self.product.name}: {self.price} AZN - {self.quantity}x"


class OrderItemSale(TimeStampedModel):
    """Model definition for OrderItemSale."""

    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="sales")
    warehouse_item = models.ForeignKey("warehouse.WarehouseItem", on_delete=models.CASCADE, related_name="sales")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Order Item Sale"
        verbose_name_plural = "Order Item Sales"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of OrderItemSale."""
        return f"{self.order_item.product.name}"


class OrderExpense(TimeStampedModel):
    """Model definition for OrderExpense."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="expenses")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Order Expense"
        verbose_name_plural = "Order Expenses"

        ordering = ("-updated_at",)

    def __str__(self):
        """Unicode representation of OrderExpense."""
        return f"Order Expense: {self.name} - {self.price} AZN"
