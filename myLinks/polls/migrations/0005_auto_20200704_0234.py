# Generated by Django 3.0.7 on 2020-07-03 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_link_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=250),
        ),
    ]
