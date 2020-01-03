from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'note', 'create_date', 'modify_date',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Customer, CustomerAdmin)
