# Generated by Django 4.2.2 on 2023-07-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]