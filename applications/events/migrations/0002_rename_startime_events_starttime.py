# Generated by Django 3.2.6 on 2021-10-28 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='startime',
            new_name='starttime',
        ),
    ]
