# Generated by Django 3.0.2 on 2020-03-09 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technics', '0002_auto_20200302_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technics',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
