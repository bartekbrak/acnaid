from django.utils.translation import ugettext_lazy as _

CMS_TEMPLATES = (
    ('main.html', _('main')),
    ('product_index.html', _('index of products')),
    ('product_details.html', _('product details')),
)

LANGUAGES = [
    ('pl', 'Polish'),
    ('en', 'English'),
]

CMS_LANGUAGES = (
    ('pl', 'PL'),
    ('en', 'EN'),
)

CMS_PLACEHOLDER_CONF = {
    'slides': {
        'name': _('Slides'),
        'plugins': 'SliderImage',
        'limits': {
            'LinkPlugin': 3
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
    'left_column_heading_2' : {
        'name': _('left_column_heading_2'),
        'plugins': 'CharFieldPlugin',
        'limits': { 'CharFieldPlugin' : 1 }
    },
    'left_column_2' : {
        'name': _('left_column_2'),
        'plugins': 'TextPlugin',
    },
    'right_column_heading_1' : {
        'name': _('right_column_heading_1'),
        'plugins': 'CharFieldPlugin',
        'limits': { 'CharFieldPlugin' : 1 }
    },
    'right_column_1' : {
        'name': _('right_column_1'),
        'plugins': 'TextPlugin',
    },
    'right_column_heading_2' : {
        'name': _('right_column_heading_2'),
        'plugins': 'CharFieldPlugin',
        'limits': { 'CharFieldPlugin' : 1 }
    },
    'right_column_2' : {
        'name': _('right_column_2'),
        'plugins': 'TextPlugin',
    },
    'invisible_visual_description':{'name':_('invisible_visual_description'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'broad_description':{'name':_('broad_description'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'name':{'name':_('name'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'name_subtitle':{'name':_('name_subtitle'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
    'description':{'name':_('description'), 'plugins':'CharFieldPlugin','limits':{'CharFieldPlugin':1}},
 }
