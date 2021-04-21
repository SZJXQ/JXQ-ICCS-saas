# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2021-04-16 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=32, verbose_name='创建者')),
                ('updator', models.CharField(max_length=32, verbose_name='修改着')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_time', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=256)),
                ('project_id', models.CharField(max_length=32)),
                ('cluster_id', models.CharField(max_length=32)),
                ('namespace', models.CharField(max_length=64)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('deployed', 'deployed'), ('failed', 'failed'), ('unknown', 'unknown')], default='pending', max_length=32)),
                ('message', models.TextField(default='')),
                ('template_id', models.IntegerField(verbose_name='关联model Template')),
            ],
            options={
                'db_table': 'templatesets_app_release',
            },
        ),
        migrations.CreateModel(
            name='ResourceInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=32, verbose_name='创建者')),
                ('updator', models.CharField(max_length=32, verbose_name='修改着')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_time', models.DateTimeField(blank=True, null=True)),
                ('kind', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=255)),
                ('namespace', models.CharField(max_length=64)),
                ('manifest', jsonfield.fields.JSONField()),
                ('version', models.CharField(max_length=255, verbose_name='模板集版本名')),
                ('revision', models.CharField(max_length=32, verbose_name='模板集版本名的修订版号')),
                ('edited', models.BooleanField(default=False, verbose_name='是否在线编辑过')),
                ('app_release', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='templatesets.AppRelease')),
            ],
            options={
                'db_table': 'templatesets_resource_instance',
            },
        ),
        migrations.AlterUniqueTogether(
            name='apprelease',
            unique_together=set([('name', 'cluster_id', 'namespace')]),
        ),
        migrations.AlterUniqueTogether(
            name='resourceinstance',
            unique_together=set([('app_release', 'kind', 'name')]),
        ),
    ]