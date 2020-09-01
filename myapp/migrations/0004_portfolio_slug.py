# Generated by Django 3.1 on 2020-08-28 17:35

import autoslug.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200828_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
