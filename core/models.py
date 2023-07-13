from django.db import models


class Contacts(models.Model):
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200, null=True, blank=True)
    house_number = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return f'{self.email}'


class Products(models.Model):
    name = models.CharField(max_length=500)
    model = models.CharField(max_length=250)
    release_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'


class BaseModel(models.Model):
    contacts = models.ForeignKey(to=Contacts, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Factory(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return f'{self.name}'


class Storage(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    provider = models.ForeignKey(to=Factory, on_delete=models.CASCADE)
    arrears_over_provider = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return f'{self.name}'


class Retail(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    provider = models.ForeignKey(to=Storage, on_delete=models.CASCADE)
    arrears_over_provider = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return f'{self.name}'


class PrivateBusinessman(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    provider = models.ForeignKey(to=Storage, on_delete=models.CASCADE)
    arrears_over_provider = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        return f'{self.name}'
