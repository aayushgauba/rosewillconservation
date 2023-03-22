# Generated by Django 4.1.5 on 2023-03-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_alter_homeslider_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Donate",
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
                ("Title", models.CharField(max_length=200)),
                ("Description", models.TextField()),
                ("MinimumAmount", models.IntegerField(blank=True)),
                ("Image", models.FileField(blank=True, upload_to="files")),
            ],
        ),
    ]
