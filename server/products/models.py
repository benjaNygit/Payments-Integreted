from tokenize import String
from django.db import models
from .utils import custom_id

# Create your models here.


class Product(models.Model):
    """Modelo Product de Producto"""

    DISCOUNTS = [
        (0, "Sin descuento"),
        (5, "%5"),
        (10, "%10"),
        (15, "%15"),
        (20, "%20"),
        (25, "%25"),
        (30, "%30"),
        (35, "%35"),
        (40, "%40"),
        (45, "%45"),
        (50, "%50"),
        (60, "%60"),
    ]

    id = models.CharField(
        primary_key=True, unique=True, max_length=16, default=custom_id
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    stock = models.PositiveBigIntegerField(default=0)
    discount = models.DecimalField(
        max_digit=2, decimal_places=0, default=0, choices=DISCOUNTS
    )

    def make_purchase(self, quantity: int, email: String):
        """Realiza la compra de un producto

        Args:
            quantity (int): Cantidad de producto
            email (String): Correo electrónico del comprador

        Raises:
            ValueError: Si no hay productos disponibles
        """
        if quantity > self.stock:
            raise ValueError("No hay stock disponible.")
        self.stock -= quantity
        Payment.objects.create(
            product=self,
            quantity=quantity,
            email=email,
            price=self.price * (1 - self.discount / 100),
        ).save()
        return

    def has_stock(self):
        """Si posee stock el producto

        Returns:
            Boolean: True si hay stock y False si no hay stock
        """
        return self.stock > 0

    def has_discount(self):
        """Si posee descuento el producto

        Returns:
            Boolean: True si tiene descuento el producto y False si no tiene descuento el producto
        """
        return self.discount > 0


class Payment(models.Model):
    """Modelo Payment de Pagos"""

    id = models.CharField(
        primary_key=True, unique=True, max_length=16, default=custom_id
    )
    product = models.ForeignKey(Product, verbose_name="Producto relacionado")
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    date_payment = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
