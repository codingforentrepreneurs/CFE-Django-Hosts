from django.conf.urls import url

from cfehosts.hostsconfig.views import www_root_redirect

urlpatterns = [
    url(r'^(?P<path>.*)', www_root_redirect),
    #url(r'^admin/', admin.site.urls),
]
