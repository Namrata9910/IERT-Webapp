# Generated by Django 2.1.5 on 2019-02-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("aside", "0006_auto_20190220_1759")]

    operations = [
        migrations.AlterField(
            model_name="facultys",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile_pics/default.jpg",
                null=True,
                upload_to="media/teachers_img/",
            ),
        )
    ]
