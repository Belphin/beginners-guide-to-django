# Generated by Django 4.1.7 on 2023-05-23 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
