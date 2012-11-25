from django.contrib import admin
from models import *

class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    search_fields = ['name', 'value',]
    ordering = ['name']

admin.site.register(MetaTag, MetaTagAdmin)
