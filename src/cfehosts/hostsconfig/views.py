from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse 
from django_hosts.resolvers import reverse as host_reverse


def www_root_redirect(request, path=None):
    print(path)
    # url_ = host_reverse("posts:list", host='blog')
    url_ = host_reverse("home", host='www', scheme='http', port='8000')
    if path is not None:
        url_ = url_ + path
    return HttpResponseRedirect(url_)