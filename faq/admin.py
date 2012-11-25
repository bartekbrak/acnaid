from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from models import *

class SubjectTranslationInlineAdmin(admin.StackedInline):
    verbose_name = _("Translation")
    verbose_name_plural = _("Translations")
    model = SubjectTranslation
    max_num = len(settings.LANGUAGES)
    extra = 1
    prepopulated_fields = {'slug': ('title',),}

class SubjectAdmin(admin.ModelAdmin):
    inlines = [SubjectTranslationInlineAdmin,]

class QuestionTranslationInlineAdmin(admin.StackedInline):
    verbose_name = _("Translation")
    verbose_name_plural = _("Translations")
    model = QuestionTranslation
    max_num = len(settings.LANGUAGES)
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionTranslationInlineAdmin,]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)

