# Generated by Django 4.0.5 on 2022-06-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='woman',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='woman',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
