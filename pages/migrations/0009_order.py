# Generated by Django 4.1.5 on 2023-04-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0008_alter_campaign_minimumamount"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("Campaign_id", models.CharField(max_length=100)),
                ("Amount", models.IntegerField()),
            ],
        ),
    ]