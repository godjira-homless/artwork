from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from artists.models import Artists
from customers.models import Customer
from appraisers.models import Appraisers

class Lots(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=False, related_name='customer_lot', on_delete=models.SET_NULL)
    appraiser = models.ForeignKey(Appraisers, null=True, blank=False, related_name='appraiser_lot', on_delete=models.SET_NULL)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                              null=True, blank=True, related_name='lot_creator', on_delete=models.CASCADE)
    modifier = models.ForeignKey(User, null=True, related_name='lot_modifier', on_delete=models.SET('1'))
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modify_date = models.DateTimeField(auto_now=True)
    code = models.PositiveIntegerField(blank=False, null=True, unique=True, validators=[MinValueValidator(600000)])
    worknumber = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    artist = models.ForeignKey(Artists, null=True, blank=True, related_name='artist_lot', on_delete=models.SET_NULL)
    desc = models.TextField(blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return str(str(self.artist))

    def get_absolute_url(self):
        return reverse('lots_list', kwargs={'slug': self.slug})