import os
from os.path import exists

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from artists.models import Artists
from customers.models import Customer
from appraisers.models import Appraisers
from technics.models import Technics


def path_and_rename(instance, filename):
    upload_to = 'images/'
    ext = "jpg"
    ph = "media/images/{}.{}".format(instance.code, ext).lower()

    if os.path.exists(ph):
        kieg_n = 1
        kieg = "_{:02d}".format(kieg_n)
        filename = '{}{}.{}'.format(instance.code, kieg, ext).lower()
        ph = "media/images/{}".format(filename)
        if os.path.exists(ph):
            while os.path.exists(ph):
                kieg_n += 1
                kieg = "_{:02d}".format(kieg_n)
                filename = '{}{}.{}'.format(instance.code, kieg, ext).lower()
                ph = "media/images/{}".format(filename)
    else:
        filename = '{}.{}'.format(instance.code, ext).lower()
    return os.path.join(upload_to, filename)


def validate_type(value):
    if value:
        pass
    else:
        raise ValidationError(
            ('%(value)s is not a selection'),
            params={'value': value},
        )


TYPE_CHOICES = (
    ('', '---------'),
    ('B', 'Bútor'),
    ('M', 'Műtárgy'),
    ('S', 'Szőnyeg'),
    ('E', 'Ezüst'),
    ('K', 'Ékszer'),
    ('O', 'Szobor'),
    ('F', 'Festmény'),
    ('G', 'Grafika'),
)



class Lots(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=False, related_name='customer_lot',
                                 on_delete=models.SET_NULL)
    appraiser = models.ForeignKey(Appraisers, null=True, blank=False, related_name='appraiser_lot',
                                  on_delete=models.SET_NULL)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True, blank=True, related_name='lot_creator', on_delete=models.CASCADE)
    modifier = models.ForeignKey(User, null=True, related_name='lot_modifier', on_delete=models.SET('1'))
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modify_date = models.DateTimeField(auto_now=True)
    code = models.PositiveIntegerField(blank=False, null=True, unique=True,
                                       validators=[MinValueValidator(600000), MaxValueValidator(699999)], )
    worknumber = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    artist = models.ForeignKey(Artists, null=True, blank=True, related_name='artist_lot', on_delete=models.SET_NULL)
    desc = models.TextField(blank=True)
    technic = models.ForeignKey(Technics, null=True, blank=True, related_name='technic_lot', on_delete=models.SET_NULL)
    type = models.CharField(blank=False, choices=TYPE_CHOICES, max_length=128, default=None, validators=[validate_type])
    size = models.CharField(max_length=255, blank=True)
    weight = models.CharField(max_length=255, blank=True)
    purchase = models.CharField(blank=True, null=True, max_length=20)
    price = models.CharField(blank=True, null=True, max_length=20)
    pay = models.CharField(blank=True, null=True, max_length=20)
    start = models.CharField(blank=True, null=True, max_length=20)
    limit = models.CharField(blank=True, null=True, max_length=20)
    note = models.TextField(blank=True)
    photo = models.ImageField(upload_to=path_and_rename, default='images/default.png', null=True, blank=True)
    vjegy = models.CharField(max_length=255, blank=True, null=True)
    # hammer = models.PositiveIntegerField(blank=True, null=True, default=0)
    # sold = models.PositiveIntegerField(blank=True, null=True, default=0)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return str(self.code)

    def get_absolute_url(self):
        return reverse('lots_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.code, Lots.objects)
        return super().save(*args, **kwargs)

    def get_unique_slug(self, id, code, obj):
        slug = slugify(code)
        unique_slug = slug
        counter = 1
        while obj.filter(slug=unique_slug).exists():
            if obj.filter(slug=unique_slug).values('id')[0]['id'] == id:
                break
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
