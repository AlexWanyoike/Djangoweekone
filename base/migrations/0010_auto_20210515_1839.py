# Generated by Django 3.2.3 on 2021-05-15 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_photo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
