# Generated by Django 4.2.4 on 2023-08-28 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_db', '0002_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='article_title',
            field=models.CharField(default='Heading', max_length=100),
        ),
    ]
