# Generated by Django 4.2.6 on 2023-11-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0012_alter_news_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]
