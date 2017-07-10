# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-10 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20170614_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=64, verbose_name='\u59d3\u540d')),
                ('phone', models.CharField(max_length=16, verbose_name='\u624b\u673a\u53f7')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('sign', models.BooleanField(verbose_name='\u7b7e\u5230\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('event', models.ForeignKey(db_column='\u5de5\u5730', on_delete=django.db.models.deletion.CASCADE, to='sign.Event', verbose_name='\u5173\u8054\u53d1\u5e03\u4f1a')),
            ],
            options={
                'verbose_name': '\u5609\u5bbe',
                'verbose_name_plural': '\u5609\u5bbe',
            },
        ),
        migrations.AlterUniqueTogether(
            name='guest1',
            unique_together=set([('event', 'phone')]),
        ),
    ]
