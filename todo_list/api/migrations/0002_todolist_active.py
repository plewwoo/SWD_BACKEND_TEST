# Generated by Django 4.2.3 on 2023-07-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]