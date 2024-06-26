# Generated by Django 5.0.1 on 2024-01-03 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Suivi", "0002_rename_nementity_animationcontact_namentity"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogInventaire",
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
                (
                    "materialName",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                ("status", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "acquisitionWay",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("amount", models.PositiveIntegerField(blank=True, null=True)),
                ("unit", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "storageLocation",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("elec", models.FloatField(default=500)),
                ("elecComment", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("location", models.CharField(max_length=20)),
                ("comment", models.TextField(blank=True, null=True)),
                ("table", models.PositiveIntegerField(blank=True, null=True)),
                ("chair", models.PositiveIntegerField(blank=True, null=True)),
                ("panel", models.PositiveIntegerField(blank=True, null=True)),
                ("panelType", models.CharField(blank=True, max_length=50, null=True)),
                ("water", models.BooleanField(blank=True, null=True)),
                ("elec", models.FloatField(default=500)),
                ("elecComment", models.TextField(blank=True, null=True)),
                ("secuCheck", models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="tresorerycompta",
            name="currency",
            field=models.CharField(blank=True, default="CHF", max_length=10, null=True),
        ),
        migrations.CreateModel(
            name="AnimationActivity",
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
                ("name", models.CharField(max_length=100)),
                ("comment", models.TextField()),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                ("descriptionComm", models.TextField()),
                ("arrivalTiming", models.DateTimeField()),
                ("staffNeeded", models.PositiveIntegerField()),
                ("staffPreRequis", models.TextField()),
                ("staffActivityDescription", models.TextField()),
                (
                    "activityMoney",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Suivi.tresorerycompta",
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Suivi.animationcontact",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnimationPrestation",
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
                ("name", models.CharField(max_length=100)),
                ("comment", models.TextField()),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                ("descriptionComm", models.TextField()),
                ("staffNeeded", models.PositiveIntegerField()),
                ("staffPreRequis", models.TextField()),
                ("staffActivityDescription", models.TextField()),
                ("technicalSheet", models.TextField()),
                ("satCheck", models.BooleanField()),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Suivi.animationcontact",
                    ),
                ),
                (
                    "prestationMoney",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Suivi.tresorerycompta",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnimationStand",
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
                ("name", models.CharField(max_length=100)),
                ("comment", models.TextField()),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                ("location", models.CharField(blank=True, max_length=20, null=True)),
                ("table", models.PositiveIntegerField(blank=True, null=True)),
                ("chair", models.PositiveIntegerField(blank=True, null=True)),
                ("panel", models.PositiveIntegerField(blank=True, null=True)),
                ("panelType", models.CharField(blank=True, max_length=50, null=True)),
                ("vaisselle", models.TextField()),
                ("water", models.BooleanField(blank=True, null=True)),
                ("elec", models.FloatField(default=500)),
                ("elecComment", models.TextField(blank=True, null=True)),
                ("secuCheck", models.BooleanField(blank=True, null=True)),
                ("deliveryTiming", models.DateTimeField()),
                ("descriptionComm", models.TextField()),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Suivi.animationcontact",
                    ),
                ),
                (
                    "standMoney",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Suivi.tresorerycompta",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Planning",
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
                ("comment", models.TextField(blank=True, null=True)),
                ("day", models.DateField()),
                ("start", models.DateTimeField()),
                ("duration", models.PositiveIntegerField()),
                ("end", models.DateTimeField(blank=True, null=True)),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Suivi.room",
                    ),
                ),
            ],
        ),
    ]
