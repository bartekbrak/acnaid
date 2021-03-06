from cms.models import CMSPlugin, Page
from django.db import models
from django.utils.translation import ugettext_lazy as _
from os.path import basename

class Slide(CMSPlugin):
    """Extends standard plugin with a second image"""

    image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
    second_image = models.ImageField(_("second image"), upload_to=CMSPlugin.get_media_path, help_text=_("this is the product tile image"))
    # url = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True)
    title = models.CharField(_("title"), max_length=255, blank=True, null=True)
    longdesc = models.CharField(_("long description"), max_length=255, blank=True, null=True)

    def __unicode__(self):
        if self.title:
            return self.title[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't defined
            try:
                return u"%s" % basename(self.image.path)
            except:
                pass
        return "<empty>"

class Product(CMSPlugin):
    """used on index of products page"""

    image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
    broad_description = models.CharField(_("broad description"), max_length=255, blank=True, null=True)
    broad_description_sub = models.CharField(_("broad description subtitle"), max_length=255, blank=True, null=True)
    name = models.CharField(_("product name"), max_length=255)
    name_subtitle = models.CharField(_("product subtitle"), max_length=255)
    description = models.TextField(_("description"), max_length=255 * 10, blank=True, null=True, help_text='No longer than 100 words.')
    page_link = models.ForeignKey(Page, verbose_name=_("page"), limit_choices_to={'publisher_is_draft': True})

    def __unicode__(self):
        return self.name


class LikesCmsPlugin(CMSPlugin):
    """TD"""

    thumb = models.ImageField(_("thumb"), upload_to=CMSPlugin.get_media_path)
    sub = models.CharField(_("subtitle"), max_length=255, help_text='HTML tags allowed.')
    image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
    description = models.TextField(_("description"), max_length=255 * 4, help_text='HTML tags allowed.')
    quote = models.CharField(_("quote"), max_length=255 * 10, help_text='HTML tags allowed.')
    chose = models.TextField(_("chose"), max_length=255 * 10, help_text='HTML tags allowed.')
    product_image = models.ImageField(_("product image"), upload_to=CMSPlugin.get_media_path)
    page_link = models.ForeignKey(Page, verbose_name=_("page"), limit_choices_to={'publisher_is_draft': True})

    def __unicode__(self):
        return self.sub
