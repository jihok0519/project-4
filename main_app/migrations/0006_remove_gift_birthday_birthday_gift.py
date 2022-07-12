# Generated by Django 4.0.5 on 2022-07-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_gift_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='birthday',
        ),
        migrations.AddField(
            model_name='birthday',
            name='gift',
            field=models.ManyToManyField(to='main_app.gift'),
        ),
    ]
