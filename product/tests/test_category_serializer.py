from rest_framework.test import APITestCase
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer

class CategorySerializerTest(APITestCase):

    def setUp(self):
        self.category_data = {
            'title': 'Electronics',
            'slug': 'electronics',
            'description': 'Electronic items',
            'active': True,
        }
        self.category = Category.objects.create(**self.category_data)

    def test_category_serializer_valid(self):
        serializer = CategorySerializer(self.category)
        self.assertEqual(serializer.data['title'], 'Electronics')
        self.assertEqual(serializer.data['slug'], 'electronics')

    def test_category_serializer_invalid(self):
        invalid_data = {
            'title': '',
            'slug': 'electronics',
            'description': 'Electronic items',
            'active': True,
        }
        serializer = CategorySerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)