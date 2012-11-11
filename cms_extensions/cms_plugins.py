# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from models import Slide, Product
from forms import ProductAdminForm



class SliderImage(CMSPluginBase):
    model = Slide
    name = _('Slider Image')
    render_template = "slider_image.html"

    def render(self, context, instance, placeholder):
        if instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'image': instance.image,
            'second_image': instance.second_image,
            'second_picture': instance.second_image,
            'longdesc': instance.longdesc,
            'title': instance.title,
            'link': link, 
            'placeholder': placeholder
        })
        return context    

plugin_pool.register_plugin(SliderImage)




class ProductPlugin(CMSPluginBase):
    name = _('Product')
    model = Product
    render_template = "product.html"
    text_enabled = False
    form = ProductAdminForm

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(ProductPlugin)