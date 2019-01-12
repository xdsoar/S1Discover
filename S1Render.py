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


def renderHTML(template, text):
    t = Template(open('template/'+template).read())
    return t.render(text)

if __name__ == "__main__":
    postContext = Context({'post_author': 'hello', 'post_content': 'here is the content'})
    a = renderHTML('s1_post_template.html', postContext)
    bodyContext = Context({'upname': 'saraba1st', 'title': 'test s1 post', 'postlist': a})
    body = renderHTML('s1_post_body_template.html', bodyContext)
    html = renderHTML('s1_base_template.html', Context({'body': body}))
    output = open('output.html', 'w')
    output.write(html)