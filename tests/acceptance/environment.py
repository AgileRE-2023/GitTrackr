import os
import django

def before_all(context):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'gittrackr.settings'
    django.setup()