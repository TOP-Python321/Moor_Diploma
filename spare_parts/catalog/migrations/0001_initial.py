# Generated by Django 4.2.7 on 2023-12-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(help_text='Введите марку а/м', max_length=45, verbose_name='Марка а/м')),
            ],
        ),
        migrations.CreateModel(
            name='ModelCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(help_text='Введите модель а/м', max_length=100, verbose_name='Модель а/м')),
                ('year', models.CharField(help_text='Введите год выпуска', max_length=10, verbose_name='Год выпуска')),
                ('brand_id', models.ForeignKey(help_text='Выберите марку а/м', on_delete=django.db.models.deletion.CASCADE, to='catalog.brands')),
            ],
        ),
        migrations.CreateModel(
            name='Rims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, help_text='Укажите производителя', max_length=50, null=True, verbose_name='Производитель')),
                ('production', models.CharField(choices=[('alloy', 'литые'), ('forged', 'кованные'), ('stamped', 'штампованные')], help_text='Укажите метод изготовления диска', max_length=12, verbose_name='Метод изготовления')),
                ('diameter', models.CharField(help_text='Укажите диаметр диска', max_length=2, verbose_name='Диаметр')),
                ('bolt_pattern', models.CharField(help_text='Укажите сверловку/разболтовку', max_length=10, verbose_name='Сверловка')),
                ('description', models.CharField(help_text='Краткое описание: состояние, количество и т.д.', max_length=100, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, help_text='Укажите цену', max_digits=8, verbose_name='Цена')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название запчасти', max_length=100, verbose_name='Название запчасти')),
                ('vendore_code', models.CharField(help_text='Должно содержать 13 символов (АА-0000...)', max_length=13, verbose_name='Артикул товара')),
                ('state', models.CharField(choices=[('perfect', 'отличное'), ('good', 'хорошее'), ('satisfactory', 'удовлетворительное')], help_text='Укажите состояние товара', max_length=20, verbose_name='Состояние товара')),
                ('detail_number', models.CharField(blank=True, help_text='Укажите номер запчасти', max_length=30, null=True, verbose_name='Номер запчасти')),
                ('photo', models.ImageField(help_text='Загрузите фото запчасти', upload_to='images', verbose_name='Фото запчасти')),
                ('price', models.DecimalField(decimal_places=2, help_text='Укажите цену', max_digits=10, verbose_name='Цена')),
                ('brand_id', models.ForeignKey(help_text='Выберите марку а/м', on_delete=django.db.models.deletion.CASCADE, to='catalog.brands', verbose_name='Марка а/м')),
                ('model_id', models.ForeignKey(help_text='Выберите модель а/м', on_delete=django.db.models.deletion.CASCADE, to='catalog.modelcar', verbose_name='Модель а/м')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(help_text='Укажите производителя', max_length=50, verbose_name='Производитель')),
                ('model', models.CharField(help_text='Укажите название модели', max_length=50, verbose_name='Модель')),
                ('size', models.CharField(help_text='Укажите соотношение высоты к ширине в формате: Ширина/Высота', max_length=15, verbose_name='Размер шины')),
                ('diameter', models.CharField(help_text='Укажите диаметр шины', max_length=2, verbose_name='Диаметр')),
                ('description', models.CharField(help_text='Краткое описание: состояние, количество и т.д.', max_length=100, verbose_name='Описание')),
                ('photo', models.ImageField(help_text='Загрузите фото шины', upload_to='images', verbose_name='Фото шины')),
                ('price', models.DecimalField(decimal_places=2, help_text='Укажите цену', max_digits=8, verbose_name='Цена')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SpareState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('stock', 'на складе'), ('reserve', 'резерв')], help_text='Изменить состояние заказа', max_length=10, verbose_name='Состояние заказа')),
                ('spares_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.sparepart')),
            ],
        ),
    ]
