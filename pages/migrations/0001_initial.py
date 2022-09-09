# Generated by Django 3.1.7 on 2021-03-27 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=120)),
                ('headline', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=150)),
                ('image_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BodyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.blogsmodel')),
            ],
        ),
    ]
