# Generated by Django 4.2.3 on 2023-08-08 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_spaces_alter_passworditems_other_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Spaces',
            new_name='Space',
        ),
    ]
