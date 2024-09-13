# Generated by Django 5.1.1 on 2024-09-13 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.post')),
            ],
        ),
    ]
