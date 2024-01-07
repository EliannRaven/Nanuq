# Generated by Django 5.0.1 on 2024-01-07 09:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Suivi", "0005_allergy_comment_parking_comment_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="animationactivity",
            name="imageComm",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="animationprestation",
            name="imageComm",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="animationstand",
            name="imageComm",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="room",
            name="conformation",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="animationactivity",
            name="arrivalTiming",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationactivity",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationactivity",
            name="descriptionComm",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationactivity",
            name="staffActivityDescription",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationactivity",
            name="staffNeeded",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationactivity",
            name="staffPreRequis",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationcontact",
            name="hotelStatus",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NOT_STARTED", "Pas commencé"),
                    ("WAITING_CONTACT", "En attente du contact"),
                    ("WAITING_COMMITTEE", "En attente de nous"),
                    ("OK", "Affaire conclue"),
                    ("CANCELLED", "Annulé"),
                ],
                default="NOT_STARTED",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="animationcontact",
            name="status",
            field=models.CharField(
                choices=[
                    ("NOT_STARTED", "Pas commencé"),
                    ("WAITING_CONTACT", "En attente du contact"),
                    ("WAITING_COMMITTEE", "En attente de nous"),
                    ("FORM_SENT", "Formulaire envoyé"),
                    ("FORM_ANSWERED", "Formulaire répondu"),
                    ("CONTRACT_TO_SEND", "Contrat à envoyer"),
                    ("WAITING_CONTRACT", "Contrat envoyé"),
                    ("CONTRACT_SIGNED", "Contrat signé"),
                    ("CONTRACT_CANCELLED", "Contrat annulé"),
                    ("CANCELLED", "Contact annulé"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="animationcontact",
            name="transportStatus",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NOT_STARTED", "Pas commencé"),
                    ("WAITING_CONTACT", "En attente du contact"),
                    ("WAITING_COMMITTEE", "En attente de nous"),
                    ("OK", "Affaire conclue"),
                    ("CANCELLED", "Annulé"),
                ],
                default="NOT_STARTED",
                max_length=100,
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="animationcontact",
            name="userInCharge",
        ),
        migrations.AlterField(
            model_name="animationprestation",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationprestation",
            name="descriptionComm",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationprestation",
            name="satCheck",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationprestation",
            name="staffActivityDescription",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationprestation",
            name="staffNeeded",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationprestation",
            name="staffPreRequis",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationprestation",
            name="technicalSheet",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationstand",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationstand",
            name="deliveryTiming",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationstand",
            name="descriptionComm",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animationstand",
            name="elec",
            field=models.FloatField(blank=True, default=500, null=True),
        ),
        migrations.AlterField(
            model_name="animationstand",
            name="panelType",
            field=models.CharField(
                blank=True,
                choices=[("WOOD", "Bois"), ("FELT", "Feutre"), ("METAL", "Métal")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="animationstand",
            name="vaisselle",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="panelType",
            field=models.CharField(
                blank=True,
                choices=[("WOOD", "Bois"), ("FELT", "Feutre"), ("METAL", "Métal")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="tresorerybudget",
            name="amount",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tresorerybudget",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tresorerybudget",
            name="spent",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="animationcontact",
            name="userInCharge",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]