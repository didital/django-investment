# Generated by Django 3.2.8 on 2021-11-07 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment_app', '0004_auto_20211107_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trx_date', models.DateField()),
                ('buysell', models.CharField(choices=[('B', 'BUY'), ('S', 'SELL')], max_length=1)),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inv_ref', to='investment_app.investment')),
            ],
            options={
                'ordering': ['-trx_date'],
            },
        ),
    ]
