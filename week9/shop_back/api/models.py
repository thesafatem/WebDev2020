from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, default="")

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
    # plural name


class Product(models.Model):
    name = models.CharField(max_length=200, default="prod")
    price = models.FloatField(default=0)
    description = models.TextField(default="")
    count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }
