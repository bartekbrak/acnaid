from django import forms
from django.contrib.localflavor.pl.forms import PLProvinceSelect, PLPostalCodeField
from django.utils.translation import ugettext_lazy as _
from models import *


class LocalityForm(forms.ModelForm):

    voivodeship = forms.CharField(label=_("Voivodeship"), widget=PLProvinceSelect())

    class Meta:
        model = Locality


class StoreForm(forms.ModelForm):

    postal_code = PLPostalCodeField(label=_("Postal code"))

    class Meta:
        model = Store
