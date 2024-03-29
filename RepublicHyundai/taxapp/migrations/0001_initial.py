# Generated by Django 2.1 on 2019-09-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('fin_id', models.AutoField(primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=20)),
                ('fin_date_from', models.DateField()),
                ('fin_date_to', models.DateField()),
            ],
            options={
                'db_table': 'financial_year',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TaxMaster',
            fields=[
                ('tax_master_id', models.AutoField(primary_key=True, serialize=False)),
                ('tax_product_category', models.CharField(max_length=40)),
                ('tax_hsn', models.CharField(max_length=10)),
                ('tax_sgst', models.FloatField()),
                ('tax_cgst', models.FloatField()),
                ('tax_igst', models.FloatField()),
            ],
            options={
                'db_table': 'tax_master',
                'managed': True,
            },
        ),
    ]
