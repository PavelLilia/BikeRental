# Generated by Django 4.2.6 on 2023-11-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0011_alter_news_created_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateField(),
        ),
    ]