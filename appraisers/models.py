from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Appraisers(models.Model):
    name = models.CharField(max_length=120, blank=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, related_name='appraiser_creator', on_delete=models.SET('1'))
    modified_by = models.ForeignKey(User, null=True, related_name='appraiser_modifier', on_delete=models.SET('1'))
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('update_appraiser', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.name, Appraisers.objects)
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
