# Generated by Django 2.1 on 2019-10-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropartdetails',
            name='ro_part_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
