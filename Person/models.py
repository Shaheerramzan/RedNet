from django.db import models


# Create your models here.

class Phone(models.Model):
    phone_number_1 = models.CharField(max_length=11)
    phone_number_2 = models.CharField(max_length=11)
    phone_number_3 = models.CharField(max_length=11)


class Person(models.Model):
    date_of_birth = models.DateField(null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=6, null=True)
    blood_group = models.CharField(max_length=3, null=True)
    picture = models.CharField(max_length=20, null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    profile_completed = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True)

    def set_password(self, password):
        self.password = password


class Friend(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person')
    friend = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friend')
