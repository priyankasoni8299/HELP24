# Generated by Django 2.2b1 on 2019-04-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsinfo',
            name='Time',
        ),
        migrations.AlterField(
            model_name='newsinfo',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
