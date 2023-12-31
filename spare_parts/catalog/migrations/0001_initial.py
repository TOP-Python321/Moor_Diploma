# Generated by Django 4.2.7 on 2023-12-06 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(help_text='Введите бренд', max_length=45, verbose_name='Название бренда')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('spare part', 'деталь авто'), ('tires', 'шины'), ('rims', 'диски')], help_text='Выберите категорию товара', max_length=15, verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите название товара', max_length=50, verbose_name='Название товара')),
                ('vendor_code', models.CharField(help_text='Укажите артикул товара', max_length=20, verbose_name='Артикул товара')),
                ('detail_number', models.CharField(blank=True, help_text='Укажите номер детали', max_length=45, null=True, verbose_name='Номер детали')),
                ('description', models.TextField(help_text='Укажите краткое описание товара', max_length=300, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, help_text='Укажите цену', max_digits=10, verbose_name='Цена')),
                ('brand_id', models.ForeignKey(help_text='Выберите бренд', on_delete=django.db.models.deletion.CASCADE, to='catalog.brand', verbose_name='Бренд')),
                ('category_id', models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Карточка товара',
                'verbose_name_plural': 'Карточки товара',
                'db_table': 'product_card',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(choices=[('stock', 'на складе'), ('reserved', 'в резерве'), ('sold out', 'продано')], default='stock', help_text='Укажите статус товара', max_length=10, verbose_name='Статус товара')),
            ],
            options={
                'verbose_name': 'Статус товара',
                'verbose_name_plural': 'Статусы товаров',
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='WheelDiameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.IntegerField(help_text='Укажите диаметр колеса', verbose_name='Диаметр колеса')),
            ],
            options={
                'verbose_name': 'Диаметр колеса',
                'verbose_name_plural': 'Диаметры колес',
                'db_table': 'wheel_diameter',
            },
        ),
        migrations.CreateModel(
            name='WheelSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(help_text='Укажите соотношение высоты к ширине (для шины)', max_length=100, verbose_name='Размер колеса')),
            ],
            options={
                'verbose_name': 'Размер колеса',
                'verbose_name_plural': 'Размеры колес',
                'db_table': 'wheel_size',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(help_text='Введите модель', max_length=100, verbose_name='Модель товара')),
                ('year', models.CharField(help_text='Введите год выпуска или поколение', max_length=30, verbose_name='Год выпуска(поколение)')),
                ('brand_id', models.ForeignKey(help_text='Выберите бренд', on_delete=django.db.models.deletion.CASCADE, to='catalog.brand')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
                'db_table': 'product_model',
            },
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_card_id', models.ForeignKey(help_text='Выберите товар', on_delete=django.db.models.deletion.CASCADE, to='catalog.productcard', verbose_name='Товар')),
                ('status_id', models.ForeignKey(help_text='Выберите статус товара', on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус товара')),
            ],
            options={
                'verbose_name': 'Информация о статусе товара',
                'verbose_name_plural': 'Информация о статусах товаров',
                'db_table': 'product_instance',
            },
        ),
        migrations.AddField(
            model_name='productcard',
            name='product_model_id',
            field=models.ForeignKey(blank=True, help_text='Выберите модель', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.productmodel', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='productcard',
            name='wheel_diameter_id',
            field=models.ForeignKey(blank=True, help_text='Выберите диаметр колеса', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.wheeldiameter', verbose_name='Диаметр колеса'),
        ),
        migrations.AddField(
            model_name='productcard',
            name='wheel_size_id',
            field=models.ForeignKey(blank=True, help_text='Выберите размер шины', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.wheelsize', verbose_name='Размер шины'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(help_text='Загрузите фото', upload_to='images', verbose_name='Фото')),
                ('product_card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.productcard')),
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Фото товаров',
                'db_table': 'photo',
            },
        ),
    ]
