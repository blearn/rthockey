# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_article_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 8, 1, 28, 13, 84729, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=False,
        ),
    ]
