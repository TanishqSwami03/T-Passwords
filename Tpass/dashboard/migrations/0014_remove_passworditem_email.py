# Generated by Django 4.2.3 on 2024-06-04 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_passworditem_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passworditem',
            name='email',
        ),
    ]
