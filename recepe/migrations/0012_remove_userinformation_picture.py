# Generated by Django 5.0.6 on 2024-10-04 13:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recepe", "0011_userinformation_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userinformation",
            name="Picture",
        ),
    ]
