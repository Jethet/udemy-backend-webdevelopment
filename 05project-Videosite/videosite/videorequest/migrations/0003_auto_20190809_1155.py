# Generated by Django 2.2.2 on 2019-08-09 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videorequest', '0002_auto_20190805_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='videodescr',
            new_name='videodesc',
        ),
    ]
