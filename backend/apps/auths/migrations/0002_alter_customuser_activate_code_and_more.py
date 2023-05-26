# Generated by Django 4.2.1 on 2023-05-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auths", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="activate_code",
            field=models.CharField(max_length=40, verbose_name="activation code"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="is active"),
        ),
    ]
