# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Subject'
        db.create_table('faq_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('faq', ['Subject'])

        # Adding model 'SubjectTranslation'
        db.create_table('faq_subjecttranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['faq.Subject'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('faq', ['SubjectTranslation'])

        # Adding model 'Question'
        db.create_table('faq_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['faq.Subject'])),
        ))
        db.send_create_signal('faq', ['Question'])

        # Adding model 'QuestionTranslation'
        db.create_table('faq_questiontranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['faq.Question'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('faq', ['QuestionTranslation'])

        # Adding model 'FaqCmsPlugin'
        db.create_table('cmsplugin_faqcmsplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cms_plugins', to=orm['faq.Subject'])),
        ))
        db.send_create_signal('faq', ['FaqCmsPlugin'])


    def backwards(self, orm):
        
        # Deleting model 'Subject'
        db.delete_table('faq_subject')

        # Deleting model 'SubjectTranslation'
        db.delete_table('faq_subjecttranslation')

        # Deleting model 'Question'
        db.delete_table('faq_question')

        # Deleting model 'QuestionTranslation'
        db.delete_table('faq_questiontranslation')

        # Deleting model 'FaqCmsPlugin'
        db.delete_table('cmsplugin_faqcmsplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'faq.faqcmsplugin': {
            'Meta': {'object_name': 'FaqCmsPlugin', 'db_table': "'cmsplugin_faqcmsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cms_plugins'", 'to': "orm['faq.Subject']"})
        },
        'faq.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['faq.Subject']"})
        },
        'faq.questiontranslation': {
            'Meta': {'object_name': 'QuestionTranslation'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['faq.Question']"}),
            'question': ('django.db.models.fields.TextField', [], {})
        },
        'faq.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'faq.subjecttranslation': {
            'Meta': {'object_name': 'SubjectTranslation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['faq.Subject']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        }
    }

    complete_apps = ['faq']
