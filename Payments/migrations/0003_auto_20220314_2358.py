# Generated by Django 2.2 on 2022-03-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0002_auto_20220314_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
