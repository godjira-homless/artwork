# Generated by Django 3.0.2 on 2020-03-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisers', '0003_auto_20200309_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appraisers',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
