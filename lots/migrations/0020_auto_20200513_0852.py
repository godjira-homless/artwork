# Generated by Django 3.0.5 on 2020-05-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0019_auto_20200510_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='purchase',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
