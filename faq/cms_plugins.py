from django.utils.translation import ugettext as _
from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import *

FAQ_HEADING_LEVEL = getattr(settings, 'FAQ_HEADING_LEVEL', 3)

class FaqPlugin(CMSPluginBase):
    name = _("FAQ Subject")
    model = FaqCmsPlugin
    render_template = 'faq/cms_plugins/faq_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'subject': instance.subject,
            'heading_level': FAQ_HEADING_LEVEL,
        })
        return context

plugin_pool.register_plugin(FaqPlugin)

