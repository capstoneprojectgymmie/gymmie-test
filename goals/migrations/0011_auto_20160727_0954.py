# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0010_delete_weighttrend'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=6)),
                ('maxreplunges', models.IntegerField(null=True)),
                ('maxrepsitups', models.IntegerField(null=True)),
                ('maxreppushups', models.IntegerField(null=True)),
                ('maxrepsquats', models.IntegerField(null=True)),
                ('maxrepcalfraises', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='initialtest',
            name='userpro',
        ),
        migrations.RemoveField(
            model_name='levels',
            name='initial_test',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='InitialTest',
        ),
        migrations.DeleteModel(
            name='Levels',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
