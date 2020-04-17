from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify


class Customer(models.Model):
    name = models.CharField(max_length=120, blank=False)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    sale_percent = models.IntegerField(blank=True, null=True, default=21)
    buy_percent = models.IntegerField(blank=True, null=True, default=15)
    phone = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    taxnumber = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                              null=True, blank=True, related_name='customer_creator', on_delete=models.CASCADE)
    modifier = models.ForeignKey(User, null=True, related_name='customer_modifier', on_delete=models.SET_NULL)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('update_customer', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.name, Customer.objects)
        return super().save(*args, **kwargs)

    def get_unique_slug(self, id, name, obj):
        slug = slugify(name)
        unique_slug = slug
        counter = 1
        while obj.filter(slug=unique_slug).exists():
            if obj.filter(slug=unique_slug).values('id')[0]['id'] == id:
                break
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
