from django.db import models
from Person.models import Person
from Society.models import Society
# Create your models here.


class SocietyAdmin(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)


class Complain(models.Model):
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person1')
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person2')
    complain_message = models.CharField(max_length=500, null=True)
