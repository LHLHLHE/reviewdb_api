# Generated by Django 4.2 on 2023-04-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/images/', verbose_name='Фото'),
        ),
    ]
