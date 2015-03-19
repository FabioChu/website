# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measureTools', '0002_gridftptool'),
    ]

    operations = [
        migrations.CreateModel(
            name='wgetTool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_remoto', models.CharField(default=b'172.20.5.20', max_length=120)),
                ('tamanho', models.CharField(default=b'1G', max_length=120)),
                ('limite', models.CharField(default=b'1', max_length=120)),
                ('pasta_des', models.CharField(default=b'/dados/area-teste', max_length=120)),
                ('pasta_resultado', models.CharField(default=b'Resultados', max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='gridftptool',
            name='fluxo',
            field=models.CharField(default=b'1', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gridftptool',
            name='ip_remoto',
            field=models.CharField(default=b'172.20.5.20', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gridftptool',
            name='limite',
            field=models.CharField(default=b'1', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gridftptool',
            name='pasta_des',
            field=models.CharField(default=b'/dados/area-teste', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gridftptool',
            name='pasta_ori',
            field=models.CharField(default=b'~/Documents', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gridftptool',
            name='pasta_resultado',
            field=models.CharField(default=b'Resultados', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gridftptool',
            name='tamanho',
            field=models.CharField(default=b'1G', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scptool',
            name='ip_remoto',
            field=models.CharField(default=b'172.20.5.20', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scptool',
            name='limite',
            field=models.CharField(default=b'1', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scptool',
            name='pasta_des',
            field=models.CharField(default=b'/dados/area-teste', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scptool',
            name='pasta_ori',
            field=models.CharField(default=b'~/Documents', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scptool',
            name='pasta_resultado',
            field=models.CharField(default=b'Resultados', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scptool',
            name='tamanho',
            field=models.CharField(default=b'1G', max_length=120),
            preserve_default=True,
        ),
    ]
