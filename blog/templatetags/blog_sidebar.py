'''
Created on Nov 22, 2011

@author: Khazidhea
'''

from django import template
register = template.Library()

from blog.models import *

@register.inclusion_tag('blog/categories.html')
def blog_categories():
    return {
        'categories': Category.objects.all(),
    }

@register.inclusion_tag('blog/archive.html')
def blog_archive():
    return {
        'archives': Post.objects.dates('published', 'month', order='DESC'),
    }