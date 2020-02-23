from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from artists.models import Artists
from django.contrib.auth.models import User


class Extras(models.Model):
    artist = models.ForeignKey(Artists, null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              null=True, blank=True, related_name='extra_owner', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, null=True, related_name='extra_modifier', on_delete=models.SET('1'))
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    slug = models.SlugField(null=False, unique=True, default="5")

    def __str__(self):
        return str(str(self.artist))

    def get_absolute_url(self):
        return reverse('detail_lot', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # if Extras.objects.count() > 0:
        #    return
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.artist, Extras.objects)
        return super().save(*args, **kwargs)

    def get_unique_slug(self, id, title, obj):
        slug = slugify(title)
        unique_slug = slug
        counter = 1
        while obj.filter(slug=unique_slug).exists():
            if obj.filter(slug=unique_slug).values('id')[0]['id'] == id:
                break
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
