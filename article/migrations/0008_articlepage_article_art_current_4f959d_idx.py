# Generated by Django 3.2.5 on 2021-07-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_articlepage_article_art_last_mo_a81817_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='articlepage',
            index=models.Index(fields=['current_section', 'last_modified_at'], name='article_art_current_4f959d_idx'),
        ),
    ]
