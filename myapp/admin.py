from django.contrib import admin
from .models import suzlar

class suzlarAdmin(admin.ModelAdmin):
    list_display = ['inglizcha', 'uzbekcha']

admin.site.register(suzlar, suzlarAdmin)
