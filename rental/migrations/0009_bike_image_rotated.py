# Generated by Django 4.2.6 on 2023-11-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_bikecategory_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='image_rotated',
            field=models.ImageField(blank=True, upload_to='images/rotated'),
        ),
    ]
