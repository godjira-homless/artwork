from django.contrib import admin

from .models import Appraisers


class AppraiserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Appraisers, AppraiserAdmin)
