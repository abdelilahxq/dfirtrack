# Generated by Django 2.0 on 2018-09-11 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0003_default_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='system',
            old_name='system_fqdn',
            new_name='system_dnssuffix',
        ),
    ]
