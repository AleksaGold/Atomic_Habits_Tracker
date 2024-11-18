# Generated by Django 5.1.3 on 2024-11-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0008_alter_condition_frequency_alter_habit_next_sending"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание привычки"
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="name",
            field=models.CharField(max_length=150, verbose_name="Название привычки"),
        ),
    ]
