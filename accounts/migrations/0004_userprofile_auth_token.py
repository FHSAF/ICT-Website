# Generated by Django 3.2 on 2021-04-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210424_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='auth_token',
            field=models.CharField(default='3', max_length=100),
            preserve_default=False,
        ),
    ]
