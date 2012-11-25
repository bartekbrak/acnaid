from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


class ContactPlugin(CMSPlugin):

    recipient = models.EmailField(_("recipient"))

    class Meta:
        verbose_name = _("Contact plugin")
        verbose_name_plural = _("Contact plugins")

    def __unicode__(self):
        return self.recipient
