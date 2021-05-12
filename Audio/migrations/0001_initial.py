# Generated by Django 3.2.2 on 2021-05-12 09:37

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('narrator', models.CharField(max_length=100, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('uploadedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('uploadedTime', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('participants', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1010, size=10)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('uploadedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
