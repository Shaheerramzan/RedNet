from django.db import models
from Person.models import Person
# Create your models here.


class ConveyanceProvider(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    is_mute = models.BooleanField()
