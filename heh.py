from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=1000)
    description = models.CharField(max_length=255)
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.CharField(max_length=100)
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active,
            'category':self.category
        }

class Category(models.Model):
    name = models.CharField(max_length=255)

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name
        }