# Generated by Django 4.2.1 on 2023-06-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auths", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="activate_code",
            field=models.CharField(
                blank=True, max_length=40, null=True, verbose_name="activate code"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="wallet",
            field=models.CharField(
                blank=True, max_length=42, null=True, verbose_name="wallet"
            ),
        ),
    ]
