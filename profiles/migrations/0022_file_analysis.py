# Generated by Django 3.1.4 on 2020-12-20 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0021_delete_file_analysis'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Analysis',
            fields=[
                ('shareFileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='profiles.sharefile')),
                ('reading_Time', models.IntegerField(default='')),
                ('reading_Count', models.IntegerField(default='')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
