# Generated by Django 3.1.4 on 2020-12-19 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_merge_20201219_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='bla',
        ),
    ]
