# Generated by Django 3.1.1 on 2020-11-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20201104_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharefile',
            name='owner_name',
            field=models.TextField(default=''),
        ),
    ]
