# Generated by Django 4.0.1 on 2022-01-26 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_activ',
            new_name='is_active',
        ),
    ]
