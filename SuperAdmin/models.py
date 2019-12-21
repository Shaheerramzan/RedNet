from django.db import models
from Person.models import Person
# Create your models here.


class SuperAdmin(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
