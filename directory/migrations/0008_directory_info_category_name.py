# Generated by Django 2.2b1 on 2019-04-18 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_directory_info_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory_info',
            name='category_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='directory.Categories'),
            preserve_default=False,
        ),
    ]
