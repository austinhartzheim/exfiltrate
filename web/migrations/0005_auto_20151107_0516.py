# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_uploadedfile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/%Y/%m/%d', blank=True),
        ),
    ]
