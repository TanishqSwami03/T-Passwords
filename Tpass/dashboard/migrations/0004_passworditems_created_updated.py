# Generated by Django 4.2.3 on 2023-08-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_spaces_space'),
    ]

    operations = [
        migrations.AddField(
            model_name='passworditems',
            name='created_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]