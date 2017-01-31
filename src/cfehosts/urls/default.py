from django.conf.urls import url
from django.contrib import admin

from cfehosts.views import home

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
]
