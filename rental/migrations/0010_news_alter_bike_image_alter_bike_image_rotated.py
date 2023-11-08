# Generated by Django 4.2.6 on 2023-11-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0009_bike_image_rotated'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, unique=True, upload_to='images/bikes')),
                ('published', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'Newses',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(blank=True, unique=True, upload_to='images/bikes'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='image_rotated',
            field=models.ImageField(blank=True, unique=True, upload_to='images/rotated'),
        ),
    ]