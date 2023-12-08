from django.test import TestCase
from .models import Product, Payment

# Create your tests here.


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test description",
            price=100,
            stock=10,
            discount=10,
        )
        self.product_with_discount = Product.objects.create(
            name="Test Product",
            description="Test description",
            price=100,
            stock=10,
            discount=10,
        )
        self.product_without_discount = Product.objects.create(
            name="Test Product without discount",
            description="Test description",
            price=100,
            stock=10,
            discount=0,
        )

    def test_make_purchase(self):
        """Test para hacer una compra"""
        initial_stock = self.product.stock
        quantity_to_purchase = 5

        self.product.make_purchase(quantity_to_purchase, "test@example.com")

        updated_product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(updated_product.stock, initial_stock - quantity_to_purchase)

    def test_make_purchase_with_discount(self):
        """Test para hacer una compra con descuento"""
        quantity_to_purchase = 2
        price_with_discount = self.product_with_discount.price - (
            (self.product_with_discount.discount * self.product_with_discount.price)
            / 100
        )

        self.product_with_discount.make_purchase(
            quantity_to_purchase, "test@example.com"
        )

        self.assertEqual(
            Payment.objects.get(product_id=self.product_with_discount.pk).price,
            quantity_to_purchase * price_with_discount,
        )

    def test_make_purchase_without_discount(self):
        """Test para hacer una compra sin descuento"""
        quantity_to_purchase = 2
        self.product_without_discount.make_purchase(
            quantity_to_purchase, "test@example.com"
        )

        self.assertEqual(
            Payment.objects.get(product_id=self.product_without_discount.pk).price,
            self.product_without_discount.price * quantity_to_purchase,
        )

    def test_make_purchase_insufficient_stock(self):
        """Test para hacer una compra con stock insuficiente"""
        quantity_to_purchase = 15

        with self.assertRaises(ValueError):
            self.product.make_purchase(quantity_to_purchase, "test@example.com")

    def test_has_stock(self):
        """Test para saber si hay stock"""
        self.assertTrue(self.product.has_stock())

        # Variar stock
        self.product.stock = 0
        self.product.save()

        self.assertFalse(self.product.has_stock())

    def test_has_discount(self):
        """Test para saver si tiene descuento"""
        self.assertTrue(self.product.has_discount())
        self.assertFalse(self.product_without_discount.has_discount())
