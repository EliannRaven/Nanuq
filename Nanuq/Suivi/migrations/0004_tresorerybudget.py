# Generated by Django 5.0.1 on 2024-01-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Suivi", "0003_loginventaire_room_alter_tresorerycompta_currency_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TresoreryBudget",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("moneyLoad", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("amount", models.PositiveIntegerField()),
                ("spent", models.PositiveIntegerField()),
                (
                    "currency",
                    models.CharField(
                        blank=True, default="CHF", max_length=10, null=True
                    ),
                ),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "subCategory",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("pole", models.CharField(blank=True, max_length=100, null=True)),
                ("comment", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
