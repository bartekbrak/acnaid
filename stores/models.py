from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.localflavor.pl import pl_voivodeships


class Locality(models.Model):

    name = models.CharField(_("name"), max_length=100)
    slug = models.SlugField(_("slug"))

    voivodeship = models.CharField(_("voivodeship"), max_length=50)

    class Meta:
        verbose_name = _("Locality")
        verbose_name_plural = _("Localities")
        unique_together = (
            ('name', 'voivodeship'),
            ('slug', 'voivodeship'),
        )

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.get_voivodeship_name())

    def get_voivodeship_name(self):
        try:
            return dict(pl_voivodeships.VOIVODESHIP_CHOICES)[self.voivodeship]
        except KeyError:
            return self.voivodeship
    get_voivodeship_name.short_description = _("voivodeship")


class Store(models.Model):

    name = models.CharField(_("name"), max_length=50)

    address = models.CharField(_("address"), max_length=100)
    phone = models.CharField(_("phone"), blank=True, null=True, max_length=50)
    postal_code = models.CharField(_("postal code"), max_length=10)
    locality = models.ForeignKey(Locality, related_name='stores', verbose_name=_("locality"))

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")
        unique_together = (
            ('name', 'locality', 'address'),
        )

    def __unicode__(self):
        return self.name
