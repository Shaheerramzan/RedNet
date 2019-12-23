from django.db import models


# Create your models here.


class Person(models.Model):
    date_of_birth = models.DateField()
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, null=True)
    blood_group = models.CharField(max_length=3, null=True)
    picture = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    profile_completed = models.BooleanField()


class Phone(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    phone_number_1 = models.IntegerField(db_index=True)
    phone_number_2 = models.IntegerField(null=True)
    phone_number_3 = models.IntegerField(null=True)


class Friend(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person')
    friend = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friend')
