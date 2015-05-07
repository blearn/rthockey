# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20150430_0619'),
    ]

    operations = [
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
    ]
