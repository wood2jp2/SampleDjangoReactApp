from django.db import models

# Create your models here.

# The models.Model is the object that Lead is inheriting from
class Lead(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.CharField(max_length = 300)
    phone = models.CharField(max_length = 10)
    createdAt = models.DateTimeField(auto_now_add = True)


class Person(models.Model):
    name = models.CharField(max_length = 100)
    cellPhone = models.CharField(max_length = 10)