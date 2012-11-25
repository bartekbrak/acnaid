# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Locality'
        db.create_table('stores_locality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('voivodeship', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('stores', ['Locality'])

        # Adding unique constraint on 'Locality', fields ['name', 'voivodeship']
        db.create_unique('stores_locality', ['name', 'voivodeship'])

        # Adding unique constraint on 'Locality', fields ['slug', 'voivodeship']
        db.create_unique('stores_locality', ['slug', 'voivodeship'])

        # Adding model 'Store'
        db.create_table('stores_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('locality', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stores', to=orm['stores.Locality'])),
        ))
        db.send_create_signal('stores', ['Store'])

        # Adding unique constraint on 'Store', fields ['name', 'locality', 'address']
        db.create_unique('stores_store', ['name', 'locality_id', 'address'])


    def backwards(self, orm):
        # Removing unique constraint on 'Store', fields ['name', 'locality', 'address']
        db.delete_unique('stores_store', ['name', 'locality_id', 'address'])

        # Removing unique constraint on 'Locality', fields ['slug', 'voivodeship']
        db.delete_unique('stores_locality', ['slug', 'voivodeship'])

        # Removing unique constraint on 'Locality', fields ['name', 'voivodeship']
        db.delete_unique('stores_locality', ['name', 'voivodeship'])

        # Deleting model 'Locality'
        db.delete_table('stores_locality')

        # Deleting model 'Store'
        db.delete_table('stores_store')


    models = {
        'stores.locality': {
            'Meta': {'unique_together': "(('name', 'voivodeship'), ('slug', 'voivodeship'))", 'object_name': 'Locality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'voivodeship': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stores.store': {
            'Meta': {'unique_together': "(('name', 'locality', 'address'),)", 'object_name': 'Store'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stores'", 'to': "orm['stores.Locality']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['stores']