# Generated by Django 4.1.3 on 2022-12-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filedatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
                ('myfiles', models.FileField(upload_to='')),
            ],
        ),
    ]