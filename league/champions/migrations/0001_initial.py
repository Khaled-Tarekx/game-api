# Generated by Django 4.0.5 on 2022-07-05 07:54

import champions.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Champion",
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
                ("name", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=50)),
                (
                    "price_rp",
                    models.IntegerField(
                        choices=[
                            (275, " 275"),
                            (975, " 975"),
                            (1350, " 1350"),
                            (1820, " 1820"),
                            (3250, " 3250"),
                        ],
                        default=975,
                    ),
                ),
                (
                    "price_be",
                    models.IntegerField(
                        choices=[
                            (450, " 450"),
                            (1350, " 1350"),
                            (3150, " 3150"),
                            (4800, " 4800"),
                            (6300, " 6300"),
                            (7800, " 7800"),
                        ],
                        default=6300,
                    ),
                ),
                (
                    "category",
                    models.IntegerField(
                        choices=[
                            (0, "Damage"),
                            (1, "Toughness"),
                            (2, "Crowd Control"),
                            (3, "Mobility"),
                            (4, "Utility"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "damage_type",
                    models.IntegerField(
                        choices=[(0, "Attack Damage"), (1, "Ability Power")], default=0
                    ),
                ),
                (
                    "difficulty",
                    models.IntegerField(
                        choices=[
                            (0, "Easy"),
                            (1, "Normal"),
                            (2, "Hard"),
                            (3, "Verydifficult"),
                        ],
                        default=1,
                    ),
                ),
                ("description", models.TextField(default="description of the item")),
                ("is_freetoplay", models.BooleanField(default=False)),
                ("disabled", models.BooleanField(default=False)),
                ("release_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ChampionAbility",
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
                ("key", models.IntegerField()),
                ("name", models.CharField(max_length=60)),
                ("is_ultimate", models.BooleanField(default=False)),
                ("description", models.TextField()),
                (
                    "video_showcase",
                    models.FileField(blank=True, null=True, upload_to=""),
                ),
            ],
            options={
                "verbose_name_plural": "Abillities",
            },
        ),
        migrations.CreateModel(
            name="ChampionMastery",
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
                ("points", models.IntegerField()),
                ("title", models.CharField(max_length=50)),
                (
                    "level",
                    models.IntegerField(
                        validators=[champions.models.validate_less_than_7]
                    ),
                ),
                (
                    "champion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="masteries",
                        to="champions.champion",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Masteries",
            },
        ),
        migrations.CreateModel(
            name="ChampionSkin",
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
                ("name", models.CharField(max_length=50)),
                (
                    "skin_rarity",
                    models.IntegerField(
                        choices=[
                            (0, "Rare"),
                            (1, "Epic"),
                            (2, "Legendary"),
                            (3, "Ultimate"),
                        ],
                        default=0,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Skins",
            },
        ),
        migrations.CreateModel(
            name="Eternal",
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
                ("score", models.IntegerField()),
                ("name", models.CharField(max_length=50)),
                (
                    "champion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="champions.champion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EternalGroup",
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
                ("name", models.CharField(max_length=50)),
                ("is_unlocked", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="SkinOwnerShip",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("paid", models.IntegerField()),
                (
                    "payment_currency",
                    models.IntegerField(choices=[(0, "Rp"), (1, "Be")], default=0),
                ),
                (
                    "skin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="champions.championskin",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EternalImage",
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
                    "eternal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="champions.eternal",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EternalGroupImage",
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
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="champions.eternalgroup",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="eternal",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="champions.eternalgroup"
            ),
        ),
        migrations.CreateModel(
            name="ChampionSkinImage",
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
                ("look", models.ImageField(default="image 2.jpg", upload_to="")),
                ("border", models.ImageField(default="image 2.jpg", upload_to="")),
                (
                    "champion_skin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="champions.championskin",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChampionOwnerShip",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("paid", models.IntegerField()),
                (
                    "payment_currency",
                    models.IntegerField(choices=[(0, "Rp"), (1, "Be")], default=1),
                ),
                (
                    "champion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="champions.champion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChampionMasteryImage",
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
                    "mastery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="champions.championmastery",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChampionImage",
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
                ("type", models.ImageField(default="image 2.jpg", upload_to="")),
                ("style", models.ImageField(default="image 2.jpg", upload_to="")),
                ("image", models.ImageField(default="image 2.jpg", upload_to="")),
                (
                    "champion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="champions.champion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChampionAbilityImage",
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
                    "champion_ability",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="champions.championability",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="champion",
            name="abilities",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="champions.championability",
            ),
        ),
        migrations.AddField(
            model_name="champion",
            name="skins",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="champions.championskin"
            ),
        ),
    ]