from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    list_display = ('title', 'published')
    prepopulated_fields = {'slug' : ('title',)}

    class Media:
        js = (
              'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
              '/static/admin/js/editor.js',
             )
        css = {
               'all': ('/static/admin/css/editor.css',),
              }

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
