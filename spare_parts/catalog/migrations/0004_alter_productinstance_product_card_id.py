# Generated by Django 4.2.7 on 2023-12-21 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_photo_product_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='product_card_id',
            field=models.ForeignKey(help_text='Выберите товар', on_delete=django.db.models.deletion.CASCADE, related_name='instance', to='catalog.productcard', verbose_name='Товар'),
        ),
    ]
