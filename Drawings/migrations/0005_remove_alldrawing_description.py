# Generated by Django 5.2.1 on 2025-05-14 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Drawings', '0004_alldrawing_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alldrawing',
            name='description',
        ),
    ]
