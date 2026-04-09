from django.core.management.base import BaseCommand
from app.models import Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if Product.objects.exists():
            print("Products already exist")
            return

        Product.objects.create(name="Laptop", price=50000)
        Product.objects.create(name="Phone", price=20000)
        Product.objects.create(name="Headphones", price=5000)

        print("Products created successfully")
