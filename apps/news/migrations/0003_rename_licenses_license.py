# Generated by Django 4.2.4 on 2023-08-14 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_gallery_licenses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Licenses',
            new_name='License',
        ),
    ]
