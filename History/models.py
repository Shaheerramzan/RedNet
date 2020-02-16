from django.db import models
from Person.models import Person


# Create your models here.


class History(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time = models.TimeField()
    completion_status = models.BooleanField()
    history_type = models.BooleanField(default=True)  # True means BloodHistory False means ConveyanceHistory
