# Generated by Django 2.2b1 on 2019-04-18 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0008_directory_info_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directory_info',
            old_name='category_name',
            new_name='category',
        ),
    ]
