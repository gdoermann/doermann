from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('doermann.common.urls')),
    (r'^resume/', include('doermann.resume.urls', 'resume')),
    (r'^', include('limbo.common.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
