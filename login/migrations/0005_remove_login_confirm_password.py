# Generated by Django 2.2b1 on 2019-04-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_login_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='confirm_password',
        ),
    ]
