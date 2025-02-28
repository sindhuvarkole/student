# Generated by Django 4.2.11 on 2024-04-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='media')),
                ('address', models.CharField(max_length=100)),
                ('marks', models.EmailField(max_length=100, unique=True)),
                ('result', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
