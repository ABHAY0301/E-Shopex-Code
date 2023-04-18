from django.db import models
from .category import Category
class Product(models.Model):
    # these all are attributes
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    description = models.CharField(max_length=200 , default=" ", null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    # Now define the methods .....    create static method
    @staticmethod #this is decorator && model = class
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    @staticmethod  # this is decorator && model = class
    def get_products_by_id(ids):
        # methods for queries kise krte h
        return Product.objects.filter(id__in = ids)