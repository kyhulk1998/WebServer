# Generated by Django 3.1.1 on 2020-11-21 16:53

from django.db import migrations
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_remove_drive_secretkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharefile',
            name='shareEmails',
            field=multi_email_field.fields.MultiEmailField(default=[]),
        ),
    ]
