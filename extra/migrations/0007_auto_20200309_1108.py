# Generated by Django 3.0.2 on 2020-03-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0006_extras_worknumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extras',
            name='worknumber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]