# Generated by Django 3.1.7 on 2021-11-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20211127_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_img',
        ),
        migrations.AddField(
            model_name='order',
            name='color',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
