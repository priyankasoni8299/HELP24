# Generated by Django 2.2b1 on 2019-04-18 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_vecancy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancyinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=50)),
                ('Contect', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_vecancy.Fields')),
            ],
        ),
    ]
