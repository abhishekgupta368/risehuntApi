# Generated by Django 3.1.1 on 2020-09-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StartUpApi', '0003_auto_20200911_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorinformation',
            name='company_invested',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='investorinformation',
            name='year_of_experience',
            field=models.IntegerField(),
        ),
    ]
