# Generated by Django 3.1.7 on 2021-11-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211101_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_review',
            name='content',
            field=models.CharField(max_length=40),
        ),
    ]