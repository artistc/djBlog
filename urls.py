# Urls
from django.conf.urls.defaults import *

# Views
from views import *

# Admin
from django.contrib import admin
from views import static_page
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^static/(.*)$', 'django.views.static.serve',
        {'document_root': 'C:/Web/Projects/djBlog/static/'}),

    # Homepage is base template with nothing else (i.e. index page)
    (r'^', include('blog.urls')),

    # Grab any word, and pass it as 'template' to static_page view
    # Not using b/c it appends .html for templates
    url(r'^(?P<template>\w+)/$', static_page, name='static_page'),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),
)
