# Generated by Django 2.2 on 2022-03-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Headshot', models.ImageField(blank=True, upload_to='assets')),
            ],
        ),
    ]
