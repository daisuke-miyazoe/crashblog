# Generated by Django 5.1.1 on 2024-09-23 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posts',
            new_name='category',
        ),
    ]
