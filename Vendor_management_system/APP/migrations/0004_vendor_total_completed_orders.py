# Generated by Django 4.2.11 on 2024-05-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_vendor_total_purchases'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='total_completed_orders',
            field=models.IntegerField(default=0, verbose_name='Total number of completed orders'),
        ),
    ]
