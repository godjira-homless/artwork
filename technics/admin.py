from django.contrib import admin
from .models import Technics


class TechnicAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'modify_date',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Technics, TechnicAdmin)
