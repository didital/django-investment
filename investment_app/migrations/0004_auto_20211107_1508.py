# Generated by Django 3.2.8 on 2021-11-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_app', '0003_auto_20211107_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='investmenttype',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='principal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
