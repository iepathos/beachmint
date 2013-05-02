# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ring'
        db.create_table('jewelry_ring', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('size', self.gf('django.db.models.fields.FloatField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('jewelry', ['Ring'])

        # Adding model 'Bracelet'
        db.create_table('jewelry_bracelet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('size', self.gf('django.db.models.fields.FloatField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('jewelry', ['Bracelet'])

        # Adding model 'Necklace'
        db.create_table('jewelry_necklace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('size', self.gf('django.db.models.fields.FloatField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('jewelry', ['Necklace'])


    def backwards(self, orm):
        # Deleting model 'Ring'
        db.delete_table('jewelry_ring')

        # Deleting model 'Bracelet'
        db.delete_table('jewelry_bracelet')

        # Deleting model 'Necklace'
        db.delete_table('jewelry_necklace')


    models = {
        'jewelry.bracelet': {
            'Meta': {'object_name': 'Bracelet'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'size': ('django.db.models.fields.FloatField', [], {}),
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
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['jewelry']