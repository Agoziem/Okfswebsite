# Generated by Django 2.2 on 2022-03-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0004_auto_20220315_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Name_of_student',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
