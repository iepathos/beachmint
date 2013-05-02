# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Necklace.type'
        db.add_column('jewelry_necklace', 'type',
                      self.gf('django.db.models.fields.CharField')(default='Necklace', max_length=50),
                      keep_default=False)

        # Adding field 'Ring.type'
        db.add_column('jewelry_ring', 'type',
                      self.gf('django.db.models.fields.CharField')(default='Ring', max_length=50),
                      keep_default=False)

        # Adding field 'Bracelet.type'
        db.add_column('jewelry_bracelet', 'type',
                      self.gf('django.db.models.fields.CharField')(default='Bracelet', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Necklace.type'
        db.delete_column('jewelry_necklace', 'type')

        # Deleting field 'Ring.type'
        db.delete_column('jewelry_ring', 'type')

        # Deleting field 'Bracelet.type'
        db.delete_column('jewelry_bracelet', 'type')


    models = {
        'jewelry.bracelet': {
            'Meta': {'object_name': 'Bracelet'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'size': ('django.db.models.fields.FloatField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Bracelet'", 'max_length': '50'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        'jewelry.necklace': {
            'Meta': {'object_name': 'Necklace'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'size': ('django.db.models.fields.FloatField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Necklace'", 'max_length': '50'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        'jewelry.ring': {
            'Meta': {'object_name': 'Ring'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'size': ('django.db.models.fields.FloatField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Ring'", 'max_length': '50'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['jewelry']