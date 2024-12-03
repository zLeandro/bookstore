from rest_framework.test import APITestCase
from product.models.product import Product
from product.models.category import Category
from product.serializers.product_serializer import ProductSerializer


class ProductSerializerTest(APITestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            title="Electronics", slug="electronics", description="Electronic items", active=True)
        self.category2 = Category.objects.create(
            title="Books", slug="books", description="Books collection", active=True)

        self.product = Product.objects.create(
            title='Smartphone',
            description='Latest model',
            price=799.99,
            active=True
        )

        self.product.category.set([self.category1, self.category2])

    def test_product_serializer_valid(self):
        serializer = ProductSerializer(self.product)
        self.assertEqual(serializer.data['title'], 'Smartphone')
        self.assertEqual(serializer.data['price'], 799.00)
        self.assertEqual(len(serializer.data['category']), 2)

    def test_product_serializer_invalid(self):
        invalid_data = {
            'title': '',
            'description': 'No title product',
            'price': 799.00,
            'active': True,
            'category': [self.category1.id]
        }
        serializer = ProductSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)