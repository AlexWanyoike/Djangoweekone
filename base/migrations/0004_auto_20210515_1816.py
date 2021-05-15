# Generated by Django 3.2.3 on 2021-05-15 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210515_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
