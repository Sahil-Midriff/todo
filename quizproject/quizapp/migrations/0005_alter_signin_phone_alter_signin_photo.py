# Generated by Django 4.1.6 on 2023-02-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_alter_signin_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='phone',
            field=models.CharField(blank=True, max_length=22, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
