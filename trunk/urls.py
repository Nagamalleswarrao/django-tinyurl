from django.conf.urls.defaults import *

from tinyurl.views import redirect

urlpatterns = patterns('',
    (r'^(?P<hash>[a-fA-F\d]{32})/$', 'tinyurl.views.redirect'),
)