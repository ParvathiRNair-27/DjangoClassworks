# Generated by Django 5.2 on 2025-06-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
