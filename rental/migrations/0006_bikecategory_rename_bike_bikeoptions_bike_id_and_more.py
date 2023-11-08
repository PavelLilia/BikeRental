# Generated by Django 4.2.6 on 2023-10-31 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_alter_bike_options_alter_bikeoptions_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='images/categories')),
                ('price', models.PositiveSmallIntegerField(default=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RenameField(
            model_name='bikeoptions',
            old_name='bike',
            new_name='bike_id',
        ),
        migrations.AddField(
            model_name='bike',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rental.bikecategory'),
            preserve_default=False,
        ),
    ]