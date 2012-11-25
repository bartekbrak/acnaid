from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from translatable.models import TranslatableModel, get_translation_model


class News(TranslatableModel):

    date = models.DateField(_("date"))
    published = models.BooleanField(_("published"), default=False)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News [plural]")

    def __unicode__(self):
        return self.get_title()

    def get_absolute_url(self):
        return reverse('news.news', kwargs={
            'year': self.date.strftime('%Y'),
            'month': self.date.strftime('%m'),
            'slug': self.get_slug(),
        })

    def get_title(self, language=None):
        return self.translated('title', "", language=language)
    get_title.short_description = _("title")

    def get_slug(self, language=None):
        return self.translated('slug', "", language=language)
    get_title.short_description = _("slug")


class NewsTranslation(get_translation_model(News, _("news"))):

    title = models.CharField(_("title"), max_length=250)
    slug = models.SlugField(_("slug"))

    content = models.TextField(_("content"))

    class Meta:
        verbose_name = _("News translation")
        verbose_name_plural = _("News translations")

    def __unicode__(self):
        return self.title


class NewsCmsPlugin(CMSPlugin):

    number_of_posts = models.PositiveIntegerField(_("number of posts"))

    class Meta:
        verbose_name = _("News CMS Plugin")
        verbose_name_plural = _("News CMS Plugins")

    def __unicode__(self):
        return "News CMS Plugin (%d posts)" % self.number_of_posts
