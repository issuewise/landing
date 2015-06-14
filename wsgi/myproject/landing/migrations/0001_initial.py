# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email of the user')),
                ('submission_time', models.DateTimeField(auto_now=True, verbose_name='time when email was submitted')),
                ('ip', models.GenericIPAddressField(verbose_name='ip address of the user at the time of     submission')),
                ('browser', models.CharField(max_length=200, verbose_name='browser used by the user at the time of     submission')),
            ],
        ),
    ]
