# Generated by Django 3.2.16 on 2024-01-05 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('rating', models.IntegerField(null=True)),
                ('publisher', models.CharField(max_length=200)),
                ('price', models.FloatField(null=True)),
                ('stock', models.IntegerField(null=True)),
            ],
        ),
    ]
