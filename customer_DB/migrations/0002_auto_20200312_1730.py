# Generated by Django 3.0.3 on 2020-03-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_DB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
