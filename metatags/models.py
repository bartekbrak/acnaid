from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

METATAGS_ALLOWED = getattr(settings, 'METATAGS_ALLOWED', (
    ('Description', 'Description'),
    ('Keywords', 'Keywords'),
    ('Author', 'Author'),
    ('Copyright', 'Copyright'),
    ('Robots', 'Robots'),
    ('Revisit-after', 'Revisit-After'),
    ('Expires', 'Expires'),
    ('Pragma', 'Pragma'),
    ('Cache-control', 'Cache-Control'),
))

class MetaTag(models.Model):

    name = models.CharField(_("name"), max_length=50, choices=METATAGS_ALLOWED, unique=True)
    value = models.TextField(_("value"))

    class Meta:
        verbose_name = _("META Tag")
        verbose_name_plural = _("META Tags")
    
    def __unicode__(self):
        return self.name

