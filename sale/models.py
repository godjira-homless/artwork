from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from customers.models import Customer
from lots.models import Lots


class Sales(models.Model):
    buyer = models.ForeignKey(Customer, null=True, blank=False, related_name='sale_buyer',
                                  on_delete=models.SET_NULL)
    code = models.ForeignKey(Lots, to_field='code', null=True, blank=False, related_name='sale_lot',
                                  on_delete=models.SET_NULL)
    purchase = models.CharField(blank=False, null=True, max_length=20)
    sold = models.CharField(blank=False, null=True, max_length=20)
    pay = models.CharField(blank=False, null=True, max_length=20)
    invoice = models.CharField(max_length=255, blank=True)
    customer_invoice = models.CharField(max_length=255, blank=True)
    vjegy = models.CharField(blank=True, null=True, max_length=20)
    sale_date = models.DateField(blank=False, null=True)
    diff = models.IntegerField(blank=True, null=True)
    tax = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True, blank=True, related_name='sale_creator', on_delete=models.CASCADE)
    modifier = models.ForeignKey(User, null=True, related_name='sale_modifier', on_delete=models.SET('1'))
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modify_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return str(str(self.code))

    def get_absolute_url(self):
        return reverse('sale_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # if Extras.objects.count() > 0:
        #    return
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.code, Sales.objects)
        return super().save(*args, **kwargs)

    def get_unique_slug(self, id, code, obj):
        slug = slugify(code)
        if slug == '':
            slug = '1'
        unique_slug = slug
        counter = 1
        while obj.filter(slug=unique_slug).exists():
            if obj.filter(slug=unique_slug).values('id')[0]['id'] == id:
                break
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

