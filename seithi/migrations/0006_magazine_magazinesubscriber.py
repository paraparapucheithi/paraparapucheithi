# Generated by Django 5.0.7 on 2025-07-26 18:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seithi', '0005_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('pdf_file', models.FileField(upload_to='magazines/')),
                ('published_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MagazineSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
