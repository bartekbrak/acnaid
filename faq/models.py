from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from translatable.models import TranslatableModel, get_translation_model

class Subject(TranslatableModel):

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

class SubjectTranslation(get_translation_model(Subject, _("subject"))):

    title = models.CharField(_("title"), max_length=150, unique=True)
    slug = models.SlugField(_("slug"), unique=True)

    class Meta:
        verbose_name = _("Subject translation")
        verbose_name_plural = _("Subject translations")

    def __unicode__(self):
        return self.title

class Question(TranslatableModel):

    subject = models.ForeignKey(Subject, related_name='questions', verbose_name=_("subject"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __unicode__(self):
        return unicode(self.get_translation())

class QuestionTranslation(get_translation_model(Question, _("question"))):

    question = models.TextField(_("question"))
    answer = models.TextField(_("answer"))

    class Meta:
        verbose_name = _("Question translation")
        verbose_name_plural = _("Question translations")

    def __unicode__(self):
        return self.question

class FaqCmsPlugin(CMSPlugin):

    subject = models.ForeignKey(Subject, related_name='cms_plugins', verbose_name=_("subject"))

    class Meta:
        verbose_name = _("FAQ CMS Plugin")
        verbose_name_plural = _("FAQ CMS Plugins")

    def __unicode__(self):
        return unicode(self.subject)

