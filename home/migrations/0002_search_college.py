# Generated by Django 2.0.6 on 2018-06-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='college',
            field=models.CharField(default='', max_length=100),
        ),
    ]
