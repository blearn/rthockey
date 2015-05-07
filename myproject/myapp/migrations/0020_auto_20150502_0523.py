# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20150430_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 5, 23, 37, 960848, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 5, 23, 47, 112146, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
    ]
