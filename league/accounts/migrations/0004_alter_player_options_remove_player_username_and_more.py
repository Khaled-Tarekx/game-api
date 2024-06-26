# Generated by Django 4.0.5 on 2022-07-05 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_player_profile"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="player",
            options={"verbose_name": "Player"},
        ),
        migrations.RemoveField(
            model_name="player",
            name="username",
        ),
        migrations.AlterField(
            model_name="player",
            name="profile",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="player",
                to="accounts.profile",
            ),
        ),
    ]
