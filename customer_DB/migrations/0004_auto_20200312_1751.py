# Generated by Django 3.0.3 on 2020-03-12 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_DB', '0003_auto_20200312_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='birthday',
            field=models.DateField(),
        ),
    ]
