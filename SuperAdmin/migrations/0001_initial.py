# Generated by Django 3.0.1 on 2019-12-23 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.Person')),
            ],
        ),
    ]