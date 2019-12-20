from django.db import models
from Person.models import Person
# Create your models here.


class Society(models.Model):
    name = models.CharField(max_length=50, null=True)
    head_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    group = models.CharField(max_length=100)
