# Generated by Django 4.0.5 on 2022-06-26 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_options_rename_time_create_post_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='user',
        ),
    ]
