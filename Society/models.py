from django.db import models
from Person.models import Person
from Donor.models import Donor


# Create your models here.
class Society(models.Model):
    name = models.CharField(max_length=50)
    head_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    group = models.CharField(max_length=100)
    # donors = models.ManyToManyField(Donor, on_delete=models.CASCADE)

