# Generated by Django 3.2.4 on 2023-09-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile_zoafup.jpg', upload_to='images/'),
        ),
    ]
