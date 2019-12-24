# Generated by Django 3.0.1 on 2019-12-23 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0001_initial'),
        ('Society', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocietyAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.Person')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society.Society')),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain_message', models.CharField(max_length=500, null=True)),
                ('person1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person1', to='Person.Person')),
                ('person2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person2', to='Person.Person')),
            ],
        ),
    ]