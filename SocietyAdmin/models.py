from django.db import models
from Person.models import Person
from Society.models import Society
# Create your models here.


class SocietyAdmin(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
