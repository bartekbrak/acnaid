from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from django.forms import ModelForm
from models import Product

class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        widgets = {
            'longdesc': WYMEditor(),
        }