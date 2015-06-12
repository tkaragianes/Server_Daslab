from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic import RedirectView
# admin.autodiscover()

from settings import MEDIA_ROOT, STATIC_ROOT, STATIC_URL
from src import views

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^index/$', views.index),
    (r'^home/$', views.index),
    (r'^research/$', views.research),
    (r'^people/$', views.people),

    (r'^resources/$', views.resources),
    (r'^contact/$', views.contact),

    # (r'^login/$', views.user_login),
    # (r'^register/$', views.register),
    # (r'^logout/$', views.user_logout),

    # (r'^ping_test/$', views.test),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT+'/media'}),
    # (r'^site_data/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
    # (r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT+'/media/admin'}),
    url(r'^(?:robots.txt)?$', 'django.views.static.serve', kwargs={'path': 'robots.txt', 'document_root': MEDIA_ROOT}),
) + static(STATIC_URL, document_root=STATIC_ROOT)

# handler404 = views.error404
# handler500 = views.error500

