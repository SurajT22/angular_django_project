# Generated by Django 5.0.1 on 2024-01-25 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_management',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelTable(
            name='user_management',
            table='user_management',
        ),
    ]
