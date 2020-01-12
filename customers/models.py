from django.db import models
from django.db.models import Q
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
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('update_customer', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


