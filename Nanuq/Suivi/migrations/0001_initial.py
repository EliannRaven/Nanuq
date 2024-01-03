# Generated by Django 5.0.1 on 2024-01-03 10:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="allergy",
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
                ("allergy", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="parking",
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
                ("parking", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="TresoreryCompta",
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
                ("moneyFlowName", models.CharField(max_length=200)),
                ("amount", models.FloatField()),
                ("currency", models.CharField(blank=True, max_length=10, null=True)),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "subCategory",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("pole", models.CharField(blank=True, max_length=100, null=True)),
                ("comment", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="AnimationContact",
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
                ("status", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("note", models.TextField(blank=True, null=True)),
                ("stand", models.BooleanField(blank=True, null=True)),
                ("activity", models.BooleanField(blank=True, null=True)),
                ("prestation", models.BooleanField(blank=True, null=True)),
                ("firstname", models.CharField(blank=True, max_length=100, null=True)),
                ("surname", models.CharField(blank=True, max_length=100, null=True)),
                ("nemEntity", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("phone", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "addressRoad",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "addressNumber",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "addressCity",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "addressCountry",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("transportComment", models.TextField(blank=True, null=True)),
                (
                    "transportStatus",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("hotelComment", models.TextField(blank=True, null=True)),
                (
                    "hotelStatus",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("allergy", models.ManyToManyField(blank=True, to="Suivi.allergy")),
                (
                    "userInCharge",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
                ("parking", models.ManyToManyField(blank=True, to="Suivi.parking")),
                (
                    "expense",
                    models.ManyToManyField(blank=True, to="Suivi.tresorerycompta"),
                ),
            ],
        ),
    ]