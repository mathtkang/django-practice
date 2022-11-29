# Generated by Django 4.1.3 on 2022-11-26 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="updated_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="updated at"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="updated at"
            ),
        ),
    ]
