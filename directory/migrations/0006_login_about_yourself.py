# Generated by Django 2.2b1 on 2019-04-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_auto_20190408_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='about_yourself',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
