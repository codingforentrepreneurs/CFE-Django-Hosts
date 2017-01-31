from django.conf.urls import url, include
#from django.contrib import admin

urlpatterns = [
    #url(r'^', admin.site.urls),
    url(r'^', include('posts.urls', namespace='posts')),
]