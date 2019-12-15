# Generated by Django 2.1 on 2019-09-29 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('prod_invent_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_total_quantity', models.IntegerField()),
                ('prod_sold_quantity', models.IntegerField()),
                ('prod_stock_remaining', models.IntegerField()),
                ('prod_amount_without_tax', models.FloatField()),
                ('prod_current_selling_price', models.FloatField()),
                ('prod_dispatch_date', models.DateField()),
                ('prod_received_date', models.DateField()),
                ('prod_location', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'product_inventory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_code', models.CharField(max_length=30)),
                ('prod_name', models.CharField(max_length=30)),
                ('prod_tag', models.CharField(blank=True, max_length=30, null=True)),
                ('prod_tax', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxapp.TaxMaster')),
            ],
            options={
                'db_table': 'product_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VendorDetails',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_code', models.CharField(max_length=45)),
                ('vendor_comp_name', models.CharField(max_length=45)),
                ('vendor_name', models.CharField(max_length=45)),
                ('vendor_office_no', models.CharField(max_length=13)),
                ('vendor_mobile_no', models.CharField(max_length=13)),
                ('vendor_email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('vendor_pan_no', models.CharField(blank=True, max_length=45, null=True)),
                ('vendor_gst_no', models.CharField(blank=True, max_length=30, null=True)),
                ('vendor_address', models.CharField(max_length=45)),
                ('vendor_city', models.CharField(max_length=20)),
                ('vendor_state', models.CharField(max_length=45)),
                ('vendor_pin_code', models.IntegerField()),
            ],
            options={
                'db_table': 'vendor_details',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='productinventory',
            name='invent_prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.ProductMaster'),
        ),
        migrations.AddField(
            model_name='productinventory',
            name='invent_vender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventoryapp.VendorDetails'),
        ),
    ]
