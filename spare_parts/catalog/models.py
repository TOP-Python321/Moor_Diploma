from django.db import models
from django.urls import reverse


class Brands(models.Model):
    """Модель, описывающая марку автомобиля"""
    brand_name = models.CharField(max_length=45, 
                                  help_text='Введите марку а/м', 
                                  verbose_name='Марка а/м')
    
    def __str__(self) -> str:
        return self.brand_name
    
    
class ModelCar(models.Model):
    """Модель, описывающая модель автомобиля"""
    model_name = models.CharField(max_length=100, 
                                  help_text='Введите модель а/м', 
                                  verbose_name='Модель а/м')
    brand_id = models.ForeignKey('Brands', 
                                 on_delete=models.CASCADE, 
                                 help_text='Выберите марку а/м', )
    year = models.CharField(max_length=10, 
                            help_text='Введите год выпуска', 
                            verbose_name='Год выпуска')
    
    def __str__(self) -> str:
        return f'{self.model_name} {self.year}'
    
    
    
class SparePart(models.Model):
    """Модель, описывающая запасную часть"""
    STATE_CHOICES = [
        ('perfect','отличное'),
        ('good', 'хорошее'),
        ('satisfactory', 'удовлетворительное')
    ]
    name = models.CharField(max_length=100,
                            help_text='Введите название запчасти',
                            verbose_name='Название запчасти')
    brand_id = models.ForeignKey('Brands',
                                 on_delete=models.CASCADE,
                                 help_text='Выберите марку а/м',
                                 verbose_name='Марка а/м')
    model_id = models.ForeignKey('ModelCar',
                                 on_delete=models.CASCADE,
                                 help_text='Выберите модель а/м',
                                 verbose_name='Модель а/м')
    vendore_code = models.CharField(max_length=13,
                                    help_text='Должно содержать 13 символов (АА-0000...)',
                                    verbose_name='Артикул товара')
    state = models.CharField(max_length=20, 
                             help_text='Укажите состояние товара',
                             verbose_name='Состояние товара',
                             choices=STATE_CHOICES)
    detail_number = models.CharField(max_length=30, 
                                     help_text='Укажите номер запчасти',
                                     verbose_name='Номер запчасти',
                                     blank=True, 
                                     null=True)
    photo = models.ImageField(upload_to='images',
                              help_text='Загрузите фото запчасти',
                              verbose_name='Фото запчасти')
    price = models.DecimalField(decimal_places=2, 
                                max_digits=10,
                                help_text='Укажите цену',
                                verbose_name='Цена')
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])
    
    
class Tires(models.Model):
    """Модель, описывающая шину"""
    brand = models.CharField(max_length=50, 
                             help_text='Укажите производителя',
                             verbose_name='Производитель')
    model = models.CharField(max_length=50,
                             help_text='Укажите название модели',
                             verbose_name='Модель',)
    size = models.CharField(max_length=15,
                            help_text='Укажите соотношение высоты к ширине в формате: Ширина/Высота',
                            verbose_name='Размер шины')
    diameter = models.CharField(max_length=2,
                                help_text='Укажите диаметр шины',
                                verbose_name='Диаметр')
    description = models.CharField(max_length=100, 
                                   help_text='Краткое описание: состояние, количество и т.д.',
                                   verbose_name='Описание')
    photo = models.ImageField(upload_to='images',
                              help_text='Загрузите фото шины',
                              verbose_name='Фото шины')
    price = models.DecimalField(decimal_places=2, 
                                max_digits=8,
                                help_text='Укажите цену',
                                verbose_name='Цена')
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return f'{self.brand} {self.model}'
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])
    
    
    
class Rims(models.Model):
    """Модель, описывающая колесный диск"""
    PRODUCTION_CHOICES = [
        ('alloy', 'литые'),
        ('forged', 'кованные'),
        ('stamped', 'штампованные')
    ]
    brand = models.CharField(max_length=50, 
                            help_text='Укажите производителя',
                            verbose_name='Производитель',
                            blank=True,
                            null=True)
    production = models.CharField(max_length=12,
                                    help_text='Укажите метод изготовления диска',
                                    verbose_name='Метод изготовления',
                                    choices=PRODUCTION_CHOICES)
    diameter = models.CharField(max_length=2,
                            help_text='Укажите диаметр диска',
                            verbose_name='Диаметр')
    bolt_pattern = models.CharField(max_length=10, 
                                    help_text='Укажите сверловку/разболтовку',
                                    verbose_name='Сверловка')
    description = models.CharField(max_length=100, 
                                help_text='Краткое описание: состояние, количество и т.д.',
                                verbose_name='Описание')
    photo = models.ImageField(upload_to='images',
                            help_text='Загрузите фото диска',
                            verbose_name='Фото шины'),
    price = models.DecimalField(decimal_places=2, 
                            max_digits=8,
                            help_text='Укажите цену',
                            verbose_name='Цена')
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.brand

    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])
        
        
class SpareState(models.Model):
    SPARES_STATE_CHOICES = [
        ('stock', 'на складе'),
        ('reserve', 'резерв')
    ]
    spares_id = models.ForeignKey('SparePart',
                                  on_delete=models.CASCADE)
    status = models.CharField(max_length=10,
                              help_text='Изменить состояние заказа',
                              verbose_name='Состояние заказа',
                              choices=SPARES_STATE_CHOICES)
    
    def __str__(self) -> str:
        return f'{self.spares_id} Статус: {self.status}'