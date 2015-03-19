# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measureTools', '0003_auto_20150318_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=120)),
                ('velocidade', models.CharField(max_length=120)),
                ('tamanho', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
