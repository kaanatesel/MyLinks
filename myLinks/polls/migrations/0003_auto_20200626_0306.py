# Generated by Django 3.0.7 on 2020-06-26 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200626_0247'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]