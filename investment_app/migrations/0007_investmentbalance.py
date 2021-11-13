# Generated by Django 3.2.8 on 2021-11-07 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment_app', '0006_auto_20211107_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentBalance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bal_inv_ref', to='investment_app.investment')),
            ],
            options={
                'ordering': ['investment__name'],
            },
        ),
    ]
