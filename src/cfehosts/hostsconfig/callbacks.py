from django.shortcuts import redirect
from django_hosts.resolvers import reverse as host_reverse

def subdomain_callback(request, username=None):
    if not username or username == "tirr":
        return redirect(host_reverse("home", host='www'))
    request.subdomain = username