# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20150419_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.RemoveField(
            model_name='image',
            name='created',
        ),
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='hidden',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='thumbnail1',
        ),
        migrations.RemoveField(
            model_name='image',
            name='thumbnail2',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=b'slick', max_length=100),
        ),
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.CharField(default=b'http://www.google.com', max_length=65535),
        ),
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='modify_date',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='customer',
            field=models.ForeignKey(to='myapp.Customer'),
        ),
        migrations.AddField(
            model_name='registration',
            name='program',
            field=models.ForeignKey(to='myapp.Program'),
        ),
        migrations.AddField(
            model_name='registration',
            name='session',
            field=models.ForeignKey(to='myapp.Session', null=True),
        ),
    ]
