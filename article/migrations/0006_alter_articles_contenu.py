# Generated by Django 4.0.5 on 2023-01-18 12:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_articles_contenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='contenu',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
