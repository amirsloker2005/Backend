# Generated by Django 5.1.4 on 2024-12-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0002_post_content_post_created_at_post_last_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='content', max_length='2000'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.URLField(default='url.com'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]
