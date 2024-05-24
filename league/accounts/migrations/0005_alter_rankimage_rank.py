# Generated by Django 4.0.5 on 2022-07-06 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_player_options_remove_player_username_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rankimage",
            name="rank",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="accounts.rank",
            ),
        ),
    ]