# Generated by Django 4.0.5 on 2022-07-09 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("champions", "0004_alter_champion_name_alter_championability_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="championmastery",
            name="profile",
        ),
        migrations.AddField(
            model_name="championmastery",
            name="player",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="masteries",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
