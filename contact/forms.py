from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):

    sender = forms.EmailField(label=_("Your e-mail"))
    content = forms.CharField(label=_("Your question"), widget=forms.Textarea())

