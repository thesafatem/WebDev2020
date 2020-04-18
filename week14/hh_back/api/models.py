from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default="")
    city = models.CharField(max_length=300)
    address = models.CharField(max_length=100, default="")

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


