# Generated by Django 2.1.5 on 2019-02-20 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aside', '0005_download_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='download_link',
            name='link',
        ),
        migrations.AddField(
            model_name='download_link',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='pdf/'),
            preserve_default=False,
        ),
    ]