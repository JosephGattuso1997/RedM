# Generated by Django 3.1 on 2020-08-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200828_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(upload_to='portfolio'),
        ),
    ]