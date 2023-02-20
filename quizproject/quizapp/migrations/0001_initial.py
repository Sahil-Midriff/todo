# Generated by Django 3.2.16 on 2023-02-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=22)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
