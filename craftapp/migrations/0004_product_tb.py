# Generated by Django 3.1.4 on 2021-02-12 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craftapp', '0003_auto_20210211_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('item', models.ImageField(default='', upload_to='img')),
                ('description', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craftapp.user_tb')),
            ],
        ),
    ]