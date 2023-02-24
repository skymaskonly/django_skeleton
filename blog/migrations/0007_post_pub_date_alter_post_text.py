# Generated by Django 4.1.7 on 2023-02-24 19:26

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_id_post_myid_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default='2020-02-01', verbose_name='published date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, db_index=True, default=blog.models.get_default_text, unique_for_date='pub_date', verbose_name='text'),
        ),
    ]