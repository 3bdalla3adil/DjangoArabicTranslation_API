# Generated by Django 4.0.5 on 2022-06-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arabic_keyword_api', '0002_alter_keyword_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='keyword_translations',
            field=models.CharField(default='لاشيء', editable=False, max_length=150, verbose_name='Ttranslated Keyword'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='keyword_text',
            field=models.CharField(max_length=150, verbose_name='KeyWord to Translate'),
        ),
    ]
