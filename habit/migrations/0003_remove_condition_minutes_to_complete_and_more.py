# Generated by Django 5.1.3 on 2024-11-14 08:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="condition",
            name="minutes_to_complete",
        ),
        migrations.AddField(
            model_name="condition",
            name="seconds_to_complete",
            field=models.PositiveSmallIntegerField(
                default=1,
                validators=[django.core.validators.MaxValueValidator(120)],
                verbose_name="Время на выполнение привычки",
            ),
            preserve_default=False,
        ),
    ]
