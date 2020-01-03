from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.text import slugify


class Customer(models.Model):
    name = models.CharField(max_length=120, blank=False)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True)
    sale_percent = models.IntegerField(blank=True, null=True, default=21)
    buy_percent = models.IntegerField(blank=True, null=True, default=15)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    note = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
