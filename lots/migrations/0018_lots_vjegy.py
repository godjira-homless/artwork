# Generated by Django 3.0.5 on 2020-05-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0017_auto_20200506_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='lots',
            name='vjegy',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]