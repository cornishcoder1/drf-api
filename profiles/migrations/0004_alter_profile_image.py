# Generated by Django 3.2.14 on 2022-07-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_hkhita', upload_to='images/'),
        ),
    ]
