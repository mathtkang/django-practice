# Generated by Django 4.1.3 on 2022-12-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0005_delete_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="updated at"),
        ),
    ]
