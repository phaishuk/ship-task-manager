# Generated by Django 4.2 on 2023-04-10 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sailors_app", "0004_alter_sailor_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sailor",
            name="position",
            field=models.ForeignKey(
                default="Simple sailor",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sailors_app.position",
            ),
        ),
    ]
