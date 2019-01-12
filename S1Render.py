import os
import django
from django.template import Template, Context, loader
from django.conf import settings

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source'
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '/template'),
)
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': TEMPLATE_DIRS
              }]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()


def renderHTML(text):
    t = Template(open('s1_template.html').read())
    c = text
    return str(t.render(c))