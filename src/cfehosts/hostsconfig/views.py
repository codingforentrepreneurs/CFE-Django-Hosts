from django.http import HttpResponseRedirect


def www_root_redirect(request, path=None):
    print(path)
    return HttpResponseRedirect("http://www.tirr.com:8000")