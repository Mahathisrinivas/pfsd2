# Generated by Django 5.0.3 on 2024-03-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0028_bookpackage_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
    ]