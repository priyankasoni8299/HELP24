# Generated by Django 2.2b1 on 2019-04-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_login_about_yourself'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory_info',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]