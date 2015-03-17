# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scpTool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_remoto', models.CharField(max_length=120)),
                ('tamanho', models.CharField(max_length=120)),
                ('limite', models.CharField(max_length=120)),
                ('pasta_ori', models.CharField(max_length=120)),
                ('pasta_des', models.CharField(max_length=120)),
                ('pasta_resultado', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
