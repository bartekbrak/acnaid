from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from models import *

class NewsTranslationInlineAdmin(admin.StackedInline):
    verbose_name = _("Translation")
    verbose_name_plural = _("Translations")
    model = NewsTranslation
    max_num = len(settings.LANGUAGES)
    extra = 1
    prepopulated_fields = {'slug': ('title',),}

class NewsAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'date', 'published',)
    list_editable = ('published',)
    search_fields = ['translations__title', 'translations__slug', 'translations__content',]
    ordering = ['-date',]
    inlines = [NewsTranslationInlineAdmin,]

admin.site.register(News, NewsAdmin)

