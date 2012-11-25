from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class NewsApp(CMSApp):
    name = _("News [plural]")
    urls = ['news.urls',]

apphook_pool.register(NewsApp)

