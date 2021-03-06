# Generated by Django 3.1.4 on 2021-02-18 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craftapp', '0006_contact_tb_rating_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='review_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(default='', max_length=30)),
                ('date', models.CharField(default='', max_length=30)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craftapp.product_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craftapp.user_tb')),
            ],
        ),
        migrations.DeleteModel(
            name='rating_tb',
        ),
    ]
