# Generated by Django 4.2.11 on 2024-03-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetlog',
            name='checkout_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
