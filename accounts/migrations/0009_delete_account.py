# Generated by Django 4.1.7 on 2023-05-24 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_account_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
