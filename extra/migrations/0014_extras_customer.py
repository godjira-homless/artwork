# Generated by Django 3.0.5 on 2020-04-26 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20200417_2229'),
        ('extra', '0013_auto_20200310_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='extras',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_extra', to='customers.Customer'),
        ),
    ]
