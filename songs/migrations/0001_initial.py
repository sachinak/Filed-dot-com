# Generated by Django 3.2.2 on 2021-05-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('uploadedTime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
