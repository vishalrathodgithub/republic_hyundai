# Generated by Django 2.1 on 2019-10-08 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0002_auto_20191009_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropartdetails',
            name='ro_part_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]