# Generated by Django 4.2.7 on 2023-12-20 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_wheeldiameter_diameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='product_card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='catalog.productcard'),
        ),
    ]
