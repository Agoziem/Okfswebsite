# Generated by Django 2.2 on 2022-03-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220322_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='Role',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='school',
            name='SchoolPhonenumber',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
