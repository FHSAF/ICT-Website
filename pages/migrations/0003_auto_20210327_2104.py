# Generated by Django 3.1.7 on 2021-03-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210327_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]