# Generated by Django 4.2 on 2023-08-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('college', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]