from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'admin', 'cfehosts.blog_urls', name='admin'),
    #host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
)




# host_patterns = [
#     host(r'www', settings.ROOT_URLCONF, name='www'),
#     host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
# ]