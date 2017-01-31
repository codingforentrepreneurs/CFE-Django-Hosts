from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'admin', 'cfehosts.urls.admin', name='admin'),
    host(r'blog', 'cfehosts.urls.blog', name='blog'),
    #host(r'blog', 'posts.urls', name='blog'),
    host(r'(?P<username>\w+)', 
            'cfehosts.hostsconfig.urls', 
            name='wildcard', 
            callback='cfehosts.hostsconfig.callbacks.subdomain_callback'
        ),
    # host(r'(\w+)', 'cfehosts.hostsconfig.urls', name='wildcard'),
)




# host_patterns = [
#     host(r'www', settings.ROOT_URLCONF, name='www'),
#     host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
# ]