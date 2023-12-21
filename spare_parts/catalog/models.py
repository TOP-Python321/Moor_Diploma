from django.db import models
from django.urls import reverse


class Brand(models.Model):
    """Модель, описывающая бренд товара"""
    
    class Meta:
        db_table = 'brand'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        
    brand_name = models.CharField(max_length=45, 
                                  help_text='Введите бренд', 
                                  verbose_name='Название бренда',
                                  editable=True)
    
    def __str__(self) -> str:
        return self.brand_name
    
    
class ProductModel(models.Model):
    """Модель, описывающая модель товара"""
    
    class Meta:
        db_table = 'product_model'
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        
    model_name = models.CharField(max_length=100, 
                                  help_text='Введите модель', 
                                  verbose_name='Модель товара',
                                  editable=True)
    brand_id = models.ForeignKey('Brand', 
                                 on_delete=models.CASCADE, 
                                 help_text='Выберите бренд', )
    year = models.CharField(max_length=30, 
                            help_text='Введите год выпуска или поколение', 
                            verbose_name='Год выпуска(поколение)',
                            editable=True)
    
    def __str__(self) -> str:
        return f'{self.brand_id} - {self.model_name} - {self.year}'
    
    
class Category(models.Model):
    """Модель, описывающая категорию товара"""
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    CATEGORY_CHOICES = [
        ('spare part', 'деталь авто'),
        ('tires', 'шины'),
        ('rims', 'диски')
    ]
    
    category = models.CharField(max_length=15,
                                help_text='Выберите категорию товара',
                                verbose_name='Категория товара',
                                choices=CATEGORY_CHOICES,
                                editable=True)
    
    def __str__(self) -> str:
        return self.category
    
    
class WheelSize(models.Model):
    """Модель, описывающая размер колеса"""
    
    class Meta:
        db_table = 'wheel_size'
        verbose_name = 'Размер колеса'
        verbose_name_plural = 'Размеры колес'
    
    size = models.CharField(max_length=100,
                            help_text='Укажите соотношение высоты к ширине (для шины)',
                            verbose_name='Размер колеса',
                            editable=True)
    
    def __str__(self) -> str:
        return self.size
    
    
class WheelDiameter(models.Model):
    """Модель, описывающая диаметр колеса"""
    
    class Meta:
        db_table = 'wheel_diameter'
        verbose_name = 'Диаметр колеса'
        verbose_name_plural = 'Диаметры колес'
    
    diameter = models.CharField(max_length=5,
                                help_text='Укажите диаметр колеса',
                                verbose_name='Диаметр колеса',
                                editable=True)
    
    def __str__(self) -> str:
        return self.diameter
    
    
class ProductCard(models.Model):
    """Модель, описывающая карточку товара"""
    
    class Meta:
        db_table = 'product_card'
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товара'
    
    title = models.CharField(max_length=50, 
                             help_text='Укажите название товара',
                             verbose_name='Название товара',
                             editable=True)
    category_id = models.ForeignKey('Category',
                                    on_delete=models.CASCADE,
                                    help_text='Выберите категорию',
                                    verbose_name='Категория товара')
    brand_id = models.ForeignKey('Brand',
                                 on_delete=models.CASCADE,
                                 help_text='Выберите бренд',
                                 verbose_name='Бренд')
    product_model_id = models.ForeignKey('ProductModel',
                                         on_delete=models.CASCADE,
                                         help_text='Выберите модель',
                                         verbose_name='Модель',
                                         blank=True,
                                         null=True)
    wheel_size_id = models.ForeignKey('WheelSize',
                                      on_delete=models.CASCADE,
                                      help_text='Выберите размер шины',
                                      verbose_name='Размер шины',
                                      blank=True,
                                      null=True)
    wheel_diameter_id = models.ForeignKey('WheelDiameter',
                                          on_delete=models.CASCADE,
                                          help_text='Выберите диаметр колеса',
                                          verbose_name='Диаметр колеса',
                                          blank=True,
                                          null=True)
    vendor_code = models.CharField(max_length=20,
                                   help_text='Укажите артикул товара',
                                   verbose_name='Артикул товара',
                                   editable=True)
    detail_number = models.CharField(max_length=45,
                                     help_text='Укажите номер детали',
                                     verbose_name='Номер детали',
                                     blank=True,
                                     null=True,
                                     editable=True)
    description = models.TextField(max_length=300,
                                   help_text='Укажите краткое описание товара',
                                   verbose_name='Описание товара',
                                   editable=True)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2,
                                help_text='Укажите цену',
                                verbose_name='Цена',
                                editable=True)
    
    def __str__(self) -> str:
        return f'{self.title} - {self.brand_id} - {self.product_model_id}'
    
    def display_brands(self):
        return ', '.join([brand.brand_name for brand in self.brand_id.all()])
    
    display_brands.short_description = 'Бренды'
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])
    
    
    
class Photo(models.Model):
    """Модель, описывающая фото товара"""
    
    class Meta:
        db_table = 'photo'
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'
    
    product_card_id = models.ForeignKey('ProductCard',
                                        on_delete=models.CASCADE,
                                        related_name='photos')
    photo = models.ImageField(upload_to='images',
                              help_text='Загрузите фото',
                              verbose_name='Фото')
    
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])


class Status(models.Model):
    """Модель, описывающая статус товара"""
    
    class Meta:
        db_table = 'status'
        verbose_name = 'Статус товара'
        verbose_name_plural = 'Статусы товаров'
    
    STATUS_CHOICES = [
        ('stock', 'на складе'),
        ('reserved', 'в резерве'),
        ('sold out', 'продано')   
    ]
    
    status_name = models.CharField(max_length=10,
                                   help_text='Укажите статус товара',
                                   verbose_name='Статус товара',
                                   choices=STATUS_CHOICES,
                                   default='stock',
                                   editable=True)
    
    def __str__(self) -> str:
        return self.status_name
    
    
class ProductInstance(models.Model):
    """Модель, описывающая информацию о статусе товара"""
    
    class Meta:
        db_table = 'product_instance'
        verbose_name = 'Информация о статусе товара'
        verbose_name_plural = 'Информация о статусах товаров'
        
        
    product_card_id = models.ForeignKey('ProductCard',
                                        on_delete=models.CASCADE,
                                        help_text='Выберите товар',
                                        verbose_name='Товар')
    status_id = models.ForeignKey('Status',
                                  on_delete=models.CASCADE,
                                  help_text='Выберите статус товара',
                                  verbose_name='Статус товара')
    
    def __str__(self) -> str:
        return f'{self.product_card_id} -- {self.status_id}'