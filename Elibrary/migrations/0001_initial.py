# Generated by Django 2.2 on 2022-03-04 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ebookimage', models.ImageField(blank=True, upload_to='assets')),
                ('EbookTitle', models.CharField(blank=True, max_length=300)),
                ('Ebookdescription', models.CharField(blank=True, max_length=400)),
                ('Ebookauthor', models.CharField(blank=True, max_length=300)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('Ebookcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subject', to='Elibrary.Subject')),
            ],
        ),
    ]
