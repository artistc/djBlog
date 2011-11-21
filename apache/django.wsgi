import os, sys

path = 'C:\Web\Projects'
sys.path.append(path)

path = 'C:\Web\Projects\djangoBlog'
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoBlog.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()