# Generated by Django 3.0.5 on 2020-05-10 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lots', '0019_auto_20200510_0829'),
        ('customers', '0003_auto_20200417_2229'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.CharField(max_length=20, null=True)),
                ('sold', models.CharField(max_length=20, null=True)),
                ('pay', models.CharField(max_length=20, null=True)),
                ('invoice', models.CharField(blank=True, max_length=255)),
                ('customer_invoice', models.CharField(blank=True, max_length=255)),
                ('vjegy', models.CharField(blank=True, max_length=20, null=True)),
                ('sale_date', models.DateField(null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_buyer', to='customers.Customer')),
                ('code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_lot', to='lots.Lots', to_field='code')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_creator', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(null=True, on_delete=models.SET('1'), related_name='sale_modifier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
