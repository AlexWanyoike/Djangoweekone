# Generated by Django 3.2.3 on 2021-05-15 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='first_name',
        ),
    ]
