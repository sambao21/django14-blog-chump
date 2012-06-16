from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from posts.views import *

urlpatterns = patterns('',
    ('^$', home),
    (r'^post/(?P<post_id>\d+)/$',post_specific),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)