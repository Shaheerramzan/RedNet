from django.db import models
from Person.models import Person
# Create your models here.


class Chat(models.Model):
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=250)
