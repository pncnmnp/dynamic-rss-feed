# Generated by Django 2.0 on 2019-06-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField()),
                ('news_url', models.URLField()),
                ('description', models.TextField()),
                ('news_category', models.CharField(max_length=100)),
            ],
        ),
    ]
