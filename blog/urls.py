# Urls
from django.conf.urls.defaults import *

# Views
from django.views.generic import list_detail
from blog.views import *
from django.views.generic import list_detail, date_based

# Models
from blog.models import Post

urlpatterns = patterns('',
     # Post detail
     url(r'post/(?P<slug>[a-z-]+)/$', blog_generic_view,
         {'redirect_to': list_detail.object_detail, 'slug_field' : 'slug', 'paginate': False},
         name='single_post'),

    # Posts by category
    url(r'^category/(\d+)$', blog_posts_by_category,
        name='blog_posts_by_category'),

    # Archives (posts by date)
    url(r'^archive/(?P<month>[a-z]+)/(?P<year>\d{4})/$', blog_generic_view,
        {'redirect_to': date_based.archive_month, 'date_field': 'published', 'template_name': 'blog/post_list.html',},
        name='blog_posts_by_month'),

    # Home page (post list)
    url(r'^$', blog_generic_view, {'redirect_to': list_detail.object_list},
        name="blog_home"),

    # Search
    url(r'^search/$', blog_post_search, name="blog_post_search"),
)
