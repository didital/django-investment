# Generated by Django 3.2.8 on 2021-11-07 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment_app', '0008_auto_20211107_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmenttypebalance',
            name='investment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bal_inv_type_ref', to='investment_app.investmenttype'),
        ),
    ]