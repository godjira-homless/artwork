# Generated by Django 3.0.5 on 2020-05-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0022_auto_20200513_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='start',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]