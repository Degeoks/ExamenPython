# Generated by Django 2.1.4 on 2018-12-08 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='idComuna',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
