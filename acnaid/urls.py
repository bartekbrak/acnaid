from django.conf.urls import patterns, include, url
from django.contrib.sites.models import Site
from django.contrib import admin
from django.conf import settings


admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nAllow: /\nDisallow: /static/website/flash/", mimetype="text/plain")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^', include('cms.urls')),  # has to be last one 
)
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += patterns('',
#         url(r'^rosetta/', include('rosetta.urls')),
#     )
