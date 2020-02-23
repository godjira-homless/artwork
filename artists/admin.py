from django.contrib import admin
from .models import Artists


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Artists, ArtistAdmin)

'''
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    ordering = ('name',)
    search_fields = ('name', 'bio')
'''
