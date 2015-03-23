# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20150311_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.CharField(default=b'd', max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Published'), (b'w', b'Withdrawn')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='program',
            name='status',
            field=models.CharField(default=b'd', max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Published'), (b'w', b'Withdrawn')]),
            preserve_default=True,
        ),
    ]
