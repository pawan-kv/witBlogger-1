# Generated by Django 2.0 on 2018-09-22 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_blog_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_id',
            new_name='user',
        ),
    ]