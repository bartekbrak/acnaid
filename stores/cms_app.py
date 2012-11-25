from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class StoresApp(CMSApp):
    name = _("Stores list")
    urls = ['stores.urls', ]

apphook_pool.register(StoresApp)
