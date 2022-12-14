# Generated by Django 4.1.2 on 2022-10-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('artist', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('audio', models.FileField(upload_to='')),
                ('duration', models.FloatField()),
            ],
        ),
    ]
