# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

CMS_TEMPLATES = (
    ('main.html', _('main')),
    ('product_index.html', _('index of products')),
    ('product_details.html', _('product details')),
    ('linia15plus.html', _('15+ line')),
    ('linia30plus.html', _('30+ line')),
    ('general.html', _('general')),
    ('stores/index.html', _('Stores List')),
)

LANGUAGES = [
    ('pl', 'Polish'),
    # ('en', 'English'),
]

CMS_LANGUAGES = (
    ('pl', 'PL'),
    # ('en', 'EN'),
)

CMS_PLACEHOLDER_CONF = {
    'slides': {
        'name': _('Slides'),
        'plugins': 'SliderImage',
        'limits': {
            'SliderImage': 3
        }
    },
    'list_of_products': {
        'name': _('Product\'s list'),
        'plugins': 'ProductPlugin',
        'limits': {
            'LinkPlugin': 2
        }
    },
    'left_column_heading_1' : {
        'name': _('left_column_heading_1'),
        'plugins': 'CharFieldPlugin',
        'limits': { 'CharFieldPlugin' : 1 }
    },
    'left_column_1' : {
        'name': _('left_column_1'),
        'plugins': 'TextPlugin',
    },
    'invisible_visual_description':{'name':_('invisible_visual_description'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'broad_description':{'name':_('broad_description'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'name':{'name':_('name'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'name_subtitle':{'name':_('name_subtitle'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'description':{'name':_('description'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    # main
    'main_slogan' : {
        'name': _('Haslo reklamowe pod sliderem'),
        'plugins': 'TextPlugin',
        'limits': { 'TextPlugin' : 1 }
    },     
    'main_slogan_under_menu' : {
        'name': _('Haslo reklamowe pod menu'),
        'plugins': 'CharFieldPlugin',
        'limits': { 'CharFieldPlugin' : 1 }
    },     
    'main_linia_15' : {
        'name': _('Opis linii 15+ '),
        'plugins': 'TextPlugin',
        'limits': { 'TextPlugin' : 1 }
    },     
    'main_linia_30' : {
        'name': _('Opis linii 30+ '),
        'plugins': 'TextPlugin',
        'limits': { 'TextPlugin' : 1 }
    },    
    # everywhere
    'footer_address' : {
        'name': _('Adres w stopce'),
        'plugins': 'TextPlugin',
        'limits': { 'TextPlugin' : 1 }
    },    
    'extra_css' : {
        'name': _('Dodatkowe style CSS'),
        'plugins': 'TextFieldPlugin',
        'limits': { 'TextFieldPlugin' : 1 }
    }, 
    # linia15plus
    'likes' : {
        'name': _('Sekcja Polubili nas'),
        'plugins': 'LikesPlugin',
        'limits': { 'LikesPlugin' : 4 }
    }, 

 }

# CharFieldPlugin
# TextFieldPlugin

