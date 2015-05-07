# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20150430_0519'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
