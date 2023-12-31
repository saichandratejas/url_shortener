# Generated by Django 4.2.5 on 2023-10-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="urlModel",
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
                ("longurl", models.CharField(max_length=255)),
                ("shorturl", models.CharField(max_length=7)),
                ("count", models.IntegerField(default=0)),
            ],
        ),
    ]
