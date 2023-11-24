# Generated by Django 4.2.7 on 2023-11-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('career', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('profile_img', models.ImageField(upload_to='about_profile_images/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]