# Generated by Django 2.2 on 2022-03-26 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0006_payment_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Level', to='SRMS.Class'),
        ),
    ]
