import factory

from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystring")
    slug = factory.Faker("pystring")
    description = factory.Faker("pystring")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker("pystring")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product