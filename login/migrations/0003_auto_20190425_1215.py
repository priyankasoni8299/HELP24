# Generated by Django 2.2b1 on 2019-04-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190419_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='about_yourself',
        ),
        migrations.AddField(
            model_name='login',
            name='confirm_password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
