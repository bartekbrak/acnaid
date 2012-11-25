# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MetaTag'
        db.create_table('metatags_metatag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('metatags', ['MetaTag'])


    def backwards(self, orm):
        
        # Deleting model 'MetaTag'
        db.delete_table('metatags_metatag')


    models = {
        'metatags.metatag': {
            'Meta': {'object_name': 'MetaTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['metatags']
