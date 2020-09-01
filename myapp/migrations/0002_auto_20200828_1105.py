# Generated by Django 3.1 on 2020-08-28 15:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[800, 600], upload_to='portfolio'),
        ),
    ]
