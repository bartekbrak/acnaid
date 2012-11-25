from django.conf.urls.defaults import *

urlpatterns = patterns('news.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[\w\-_]+)/$', 'news', name='news.news'),
    url(r'^$', 'index', name='news.index'),
)
