# Generated by Django 2.2 on 2022-04-04 00:09

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
                ('Phone_number', models.CharField(blank=True, max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=200)),
                ('Role', models.CharField(blank=True, max_length=200)),
                ('Subject', models.CharField(blank=True, max_length=200)),
                ('Class_assigned', models.CharField(blank=True, max_length=200)),
                ('Facebook_link', models.CharField(blank=True, max_length=200)),
                ('Twitter_link', models.CharField(blank=True, max_length=200)),
                ('Instagram_link', models.CharField(blank=True, max_length=200)),
                ('Headshot', models.ImageField(blank=True, upload_to='assets')),
            ],
        ),
    ]
