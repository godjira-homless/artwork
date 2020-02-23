from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Artists(models.Model):
    name = models.CharField(max_length=120, blank=False)
    bio = models.CharField(max_length=120, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, related_name='artist_creator', on_delete=models.SET('1'))
    modified_by = models.ForeignKey(User, null=True, related_name='artist_modifier', on_delete=models.SET('1'))
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    slug = models.SlugField(null=False, unique=True, default="5")

    class Meta:
        verbose_name_plural = "Művészek"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('artist_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.name, Artists.objects)
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
