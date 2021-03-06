# Generated by Django 2.2 on 2022-04-04 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Excelfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Excel', models.FileField(blank=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.ImageField(blank=True, upload_to='assets')),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(blank=True, max_length=100)),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Class', models.CharField(blank=True, max_length=10)),
                ('Subject', models.CharField(blank=True, max_length=100)),
                ('FirstTest', models.CharField(blank=True, max_length=100)),
                ('SecondTest', models.CharField(blank=True, max_length=100)),
                ('Project', models.CharField(blank=True, max_length=100)),
                ('MidTermTest', models.CharField(blank=True, max_length=100)),
                ('FirstAss', models.CharField(blank=True, max_length=100)),
                ('SecondAss', models.CharField(blank=True, max_length=100)),
                ('CA', models.CharField(blank=True, max_length=100)),
                ('Exam', models.CharField(blank=True, max_length=100)),
                ('Total', models.CharField(blank=True, max_length=100)),
                ('Grade', models.CharField(blank=True, max_length=100)),
                ('SubjectPosition', models.CharField(blank=True, max_length=5)),
                ('Remark', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=10)),
                ('Class', models.CharField(blank=True, max_length=10)),
                ('Position', models.CharField(blank=True, max_length=10)),
                ('Average', models.CharField(blank=True, max_length=10)),
                ('Password', models.CharField(blank=True, max_length=10)),
                ('Term', models.CharField(blank=True, max_length=10)),
                ('Academicsession', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
