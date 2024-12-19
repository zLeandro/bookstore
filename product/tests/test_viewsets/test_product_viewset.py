from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from product.models.product import Product, Category
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json


class TestProductViewSet(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        self.category = Category.objects.create(title="Electronics", slug="electronics")
        self.category2 = Category.objects.create(
            title="Accessories", slug="accessories"
        )

        self.token = Token.objects.create(user=self.user)

    def test_create_product(self):
        url = reverse("product-list", kwargs={"version": "v1"})

        data = {
            "title": "pro controller",
            "description": "Description of pro controller",
            "price": 200,
            "active": True,
            "categories_id": [self.category.id, self.category2.id],
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        product_data = json.loads(response.content)
        self.assertEqual(product_data["title"], data["title"])
        self.assertEqual(len(product_data["category"]), 2)
        self.assertEqual(product_data["category"][0]["title"], self.category.title)
        self.assertEqual(product_data["category"][1]["title"], self.category2.title)

    def test_get_all_product(self):
        product = Product.objects.create(
            title="pro controller",
            description="Description of pro controller",
            price=200,
            active=True,
        )
        product.category.add(self.category, self.category2)

        url = reverse("product-list", kwargs={"version": "v1"})
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)
        self.assertIn("results", product_data)
        self.assertGreater(len(product_data["results"]), 0)

        self.assertGreater(len(product_data["results"][0]["category"]), 0)
        self.assertEqual(
            product_data["results"][0]["category"][0]["title"], self.category.title
        )
        self.assertEqual(
            product_data["results"][0]["category"][1]["title"], self.category2.title
        )
