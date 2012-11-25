from django.utils.translation import ugettext as _
from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.core.mail import send_mail
from models import ContactPlugin as ContactPluginModel
from forms import ContactForm

CONTACT_FORM_SUBJECT = getattr(settings, 'CONTACT_FORM_SUBJECT', _("Contact form message"))


class ContactPlugin(CMSPluginBase):
    model = ContactPluginModel
    name = _("Contact form")
    render_template = 'contact/cms_plugins/contact_plugin.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        sent = False
        form = ContactForm()
        if request.method == 'POST':
            try:
                pid = int(request.POST['pid'])
            except (KeyError, ValueError,):
                pid = -1
            if pid == instance.id:
                form = ContactForm(request.POST)
                if form.is_valid():
                    send_mail(
                        CONTACT_FORM_SUBJECT,
                        form.cleaned_data['content'],
                        form.cleaned_data['sender'],
                        [instance.recipient, ],
                        fail_silently=True
                    )
                    sent = True
        context.update({
            'sent': sent,
            'plugin': instance,
            'form': form,
        })
        return context

plugin_pool.register_plugin(ContactPlugin)
