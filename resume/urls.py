from django.conf.urls.defaults import *

urlpatterns = patterns('doermann.resume.views',
    url(r'^$', 'index', name='index')
)
