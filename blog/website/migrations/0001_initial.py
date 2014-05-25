# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'website_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.PositiveIntegerField')(default='0')),
        ))
        db.send_create_signal(u'website', ['Article'])

        # Adding model 'Mood'
        db.create_table(u'website_mood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.PositiveIntegerField')(default='0')),
        ))
        db.send_create_signal(u'website', ['Mood'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'website_article')

        # Deleting model 'Mood'
        db.delete_table(u'website_mood')


    models = {
        u'website.article': {
            'Meta': {'object_name': 'Article'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'website.mood': {
            'Meta': {'object_name': 'Mood'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['website']