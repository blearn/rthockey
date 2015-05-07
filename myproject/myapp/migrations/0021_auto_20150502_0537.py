# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20150502_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='program',
            field=models.ForeignKey(to='myapp.Program', null=True),
        ),
    ]
