# Generated by Django 2.2 on 2019-04-06 20:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('file_sharing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtable',
            name='peer_id',
        ),
        migrations.RemoveField(
            model_name='peer',
            name='Ratings',
        ),
        migrations.RemoveField(
            model_name='peer',
            name='active',
        ),
        migrations.AddField(
            model_name='hashtable',
            name='filename',
            field=models.CharField(default=datetime.datetime(2019, 4, 6, 20, 51, 39, 138181, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reftable',
            name='Ratings',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hashtable',
            name='filehash',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='peer',
            name='peer_ip',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reftable',
            name='downloadswithpeer',
            field=models.IntegerField(default=0),
        ),
    ]