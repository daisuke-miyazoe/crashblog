# Generated by Django 5.1.1 on 2024-09-23 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_options_post_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.category'),
        ),
    ]
