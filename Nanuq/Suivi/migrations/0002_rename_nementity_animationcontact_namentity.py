# Generated by Django 5.0.1 on 2024-01-03 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Suivi", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="animationcontact",
            old_name="nemEntity",
            new_name="namEntity",
        ),
    ]
