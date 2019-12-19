from django.db import models
from Person.models import Person
# Create your models here.


class Chat(models.Model):
    person1 = models.OneToOneField(Person, on_delete=models.CASCADE)
    person2 = models.OneToOneField(Person, on_delete=models.CASCADE)
    message = models.CharField(max_length=250, null=True)
