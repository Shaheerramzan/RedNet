from django.db import models
from Person.models import Person
from Society.models import Society


# Create your models here.


class Donor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    last_donated_date = models.DateField()
    system_mute = models.BooleanField()
    is_busy = models.BooleanField()
