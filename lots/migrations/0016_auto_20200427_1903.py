# Generated by Django 3.0.5 on 2020-04-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0015_auto_20200426_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='limit',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lots',
            name='pay',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lots',
            name='price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lots',
            name='purchase',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lots',
            name='start',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
