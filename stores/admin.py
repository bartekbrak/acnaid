from django.contrib import admin
from models import *
from forms import *


class LocalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_voivodeship_name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', ]
    form = LocalityForm
    # A handy constant for the name of the alternate database.
    using = 'oliprox'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(LocalityAdmin, self).queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(LocalityAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(LocalityAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using, **kwargs)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'postal_code', 'locality',)
    ordering = ('name',)
    search_fields = ['name', 'address', 'phone', 'postal_code', 'locality__name', ]
    form = StoreForm
    # A handy constant for the name of the alternate database.
    using = 'oliprox'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(StoreAdmin, self).queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(StoreAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(StoreAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using, **kwargs)


admin.site.register(Locality, LocalityAdmin)
admin.site.register(Store, StoreAdmin)
