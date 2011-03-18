from django.conf.urls.defaults import *

urlpatterns = patterns('doermann.common.views',
    url(r'^$', 'index', name='index')
)
