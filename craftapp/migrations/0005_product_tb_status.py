# Generated by Django 3.1.4 on 2021-02-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craftapp', '0004_product_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tb',
            name='status',
            field=models.CharField(default='', max_length=30),
        ),
    ]
