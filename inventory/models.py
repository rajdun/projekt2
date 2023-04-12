from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def get_price(self):
        return round(self.price / 1000000, 2)

    def set_price(self, value):
        self.price = value * 1000000

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Call the "real" save() method
        super().save(*args, **kwargs)

        # Create an Inventory object for the product
        Inventory.objects.create(product=self, quantity=0)


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Inventory for {self.product.name}'
