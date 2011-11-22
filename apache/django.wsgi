import os, sys

path = 'C:\Web\Projects'
sys.path.append(path)

path = 'C:\Web\Projects\djBlog'
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djBlog.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()