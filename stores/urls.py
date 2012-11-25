from django.conf.urls.defaults import *

urlpatterns = patterns('stores.views',
    url(r'^$', 'index', name='stores.index'),
    url(r'^gl$', 'get_localities', name='stores.get_localities'),
    url(r'^gs$', 'get_stores', name='stores.get_stores'),
)
