# Generated by Django 3.1.5 on 2021-02-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_auto_20210210_1618"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="data_treatment",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="data treatment"
            ),
        ),
    ]
