# Generated by Django 3.1.2 on 2020-10-26 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201026_2014'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
