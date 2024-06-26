# Generated by Django 4.0.5 on 2022-07-05 07:54

import accounts.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
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
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("is_online", models.BooleanField(default=False)),
                ("level", models.IntegerField(default=1)),
                (
                    "server",
                    models.IntegerField(
                        choices=[
                            (0, "Euw"),
                            (1, "Na"),
                            (2, "China"),
                            (3, "Korea"),
                            (4, "Russia"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "friends",
                    models.ManyToManyField(
                        related_name="+", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "honor_level",
                    models.IntegerField(
                        default=2, validators=[accounts.models.validate_less_than_5]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rank",
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
                (
                    "mode",
                    models.IntegerField(
                        choices=[(0, "Solo Duo"), (1, "Flex"), (2, "Tft")], default=0
                    ),
                ),
                (
                    "rank",
                    models.CharField(
                        choices=[
                            ("UNRANKED", "Unranked"),
                            ("IRON", "Iron"),
                            ("BRONZE", "Bronze"),
                            ("SILVER", "Silver"),
                            ("GOLD", "Gold"),
                            ("PLAT", "Plat"),
                            ("DIAMOND", "Diamond"),
                            ("MASTER", "Master"),
                            ("GRANDMASTER", "Grandmaster"),
                            ("CHALENGER", "Chalenger"),
                        ],
                        default="UNRANKED",
                        max_length=11,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RankImage",
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
                ("icon", models.ImageField(default="image 2.jpg", upload_to="")),
                ("border", models.ImageField(default="image 2.jpg", upload_to="")),
                (
                    "rank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="accounts.rank",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProfileImage",
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
                (
                    "background_pick",
                    models.ImageField(default="image 2.jpg", upload_to=""),
                ),
                ("trophy", models.ImageField(default="image 2.jpg", upload_to="")),
                ("banner", models.ImageField(default="image 2.jpg", upload_to="")),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="accounts.profile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="rank",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.rank"
            ),
        ),
        migrations.CreateModel(
            name="PlayerSeasonGrade",
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
                (
                    "grade",
                    models.IntegerField(
                        choices=[
                            (0, "C Plus"),
                            (1, "B Minus"),
                            (2, "B"),
                            (3, "B Plus"),
                            (4, "A Minus"),
                            (5, "A"),
                            (6, "A Plus"),
                            (7, "S Minus"),
                            (8, "S"),
                            (9, "S Plus"),
                        ]
                    ),
                ),
                ("obtained_at", models.DateTimeField(auto_now_add=True)),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="season_grades",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlayerImage",
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
                ("icon", models.ImageField(default="image 2.jpg", upload_to="")),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("message", models.CharField(max_length=1200)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("timestamp",),
            },
        ),
        migrations.AddField(
            model_name="player",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="player",
                to="accounts.profile",
            ),
        ),
        migrations.AddField(
            model_name="player",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
