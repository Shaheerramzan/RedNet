from django.db import models
from Person.models import Person
# Create your models here.


class Report(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)



