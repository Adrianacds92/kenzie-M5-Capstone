# Generated by Django 4.1.2 on 2022-11-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=255)),
                ("number", models.IntegerField()),
                ("cep", models.CharField(max_length=8)),
                ("district", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=2)),
            ],
        ),
    ]
