# Generated by Django 3.0.5 on 2020-05-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_auto_20200511_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
