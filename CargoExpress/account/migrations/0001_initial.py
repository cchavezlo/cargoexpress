# Generated by Django 3.1.5 on 2021-02-03 13:43

import account.managers
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tenant", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=60, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=28, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=28, verbose_name="last name"
                    ),
                ),
                (
                    "registration_timestamp",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="registration timestamp"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="The telephone number must correspond to the format +49187625375 or 0187625375.",
                                regex="^\\+?\\d{7,15}$",
                            )
                        ],
                        verbose_name="phone number",
                    ),
                ),
                (
                    "terms_and_condition",
                    models.BooleanField(default=False, verbose_name="T&C"),
                ),
                (
                    "terms_and_conditions_accepted_on",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="terms and conditions accepted on",
                    ),
                ),
                (
                    "data_treatment",
                    models.BooleanField(default=False, verbose_name="data treatment"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tenant.tenant",
                        verbose_name="tenant",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
            managers=[
                ("objects", account.managers.UserManager()),
            ],
        ),
    ]
