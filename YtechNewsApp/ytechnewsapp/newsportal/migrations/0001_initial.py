# Generated by Django 2.2.6 on 2019-10-29 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ordering', models.IntegerField(default=0)),
                ('is_published', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_published', models.IntegerField(default=1)),
                ('is_editior_picked', models.IntegerField(default=0)),
                ('searching_tags', models.CharField(max_length=200)),
                ('seo_keywords', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_published', models.DateTimeField(verbose_name='date published')),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsportal.NewsCategory')),
            ],
        ),
    ]
