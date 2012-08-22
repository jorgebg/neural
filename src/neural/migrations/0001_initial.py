# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table('neural_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('neural', ['Node'])

        # Adding M2M table for field parents on 'Node'
        db.create_table('neural_node_parents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_node', models.ForeignKey(orm['neural.node'], null=False)),
            ('to_node', models.ForeignKey(orm['neural.node'], null=False))
        ))
        db.create_unique('neural_node_parents', ['from_node_id', 'to_node_id'])

        # Adding M2M table for field related on 'Node'
        db.create_table('neural_node_related', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_node', models.ForeignKey(orm['neural.node'], null=False)),
            ('to_node', models.ForeignKey(orm['neural.node'], null=False))
        ))
        db.create_unique('neural_node_related', ['from_node_id', 'to_node_id'])

    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table('neural_node')

        # Removing M2M table for field parents on 'Node'
        db.delete_table('neural_node_parents')

        # Removing M2M table for field related on 'Node'
        db.delete_table('neural_node_related')

    models = {
        'neural.node': {
            'Meta': {'object_name': 'Node'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'children'", 'symmetrical': 'False', 'to': "orm['neural.Node']"}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_rel_+'", 'to': "orm['neural.Node']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['neural']