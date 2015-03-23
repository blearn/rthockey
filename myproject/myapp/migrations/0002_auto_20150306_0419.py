# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 4, 18, 37, 661242, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 4, 19, 9, 587318, tzinfo=utc), verbose_name=b'date last modified'),
            preserve_default=False,
        ),
    ]
