# Generated by Django 4.2.4 on 2023-09-09 08:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
