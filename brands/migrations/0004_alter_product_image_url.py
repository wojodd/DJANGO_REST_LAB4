# Generated by Django 4.0.6 on 2022-07-31 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_alter_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(),
        ),
    ]
