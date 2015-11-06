# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20151105_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(1970, 1, 1, 0, 0)),
            preserve_default=False,
        ),
    ]
