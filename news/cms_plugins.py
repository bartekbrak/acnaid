from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import *


class NewsPlugin(CMSPluginBase):
    name = _("Latest news")
    model = NewsCmsPlugin
    render_template = 'news/cms_plugins/news_plugin.html'

    def render(self, context, instance, placeholder):
        news = News.objects.filter(published=True).order_by('-date')[:instance.number_of_posts]
        context.update({
            'plugin': instance,
            'news': news,
        })
        return context

plugin_pool.register_plugin(NewsPlugin)
