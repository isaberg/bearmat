# Generated by Django 2.0.5 on 2018-08-03 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bearmat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='broker',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='search',
            old_name='veteran',
            new_name='user',
        ),
    ]
