# Generated by Django 3.1.4 on 2021-02-20 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('craftapp', '0008_auto_20210218_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review_tb',
            old_name='userid',
            new_name='user_id',
        ),
    ]