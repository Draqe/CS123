# Generated by Django 2.1.2 on 2018-11-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20181112_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='evalform',
            name='Rating',
            field=models.IntegerField(default=10),
        ),
    ]
