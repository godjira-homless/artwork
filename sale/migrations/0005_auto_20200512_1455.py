# Generated by Django 3.0.5 on 2020-05-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_auto_20200512_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
