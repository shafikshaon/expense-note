# Generated by Django 5.0.6 on 2024-05-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_systemuser_role_alter_systemuser_added_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="systemuser",
            name="code",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
