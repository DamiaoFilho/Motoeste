from django.db import models
#from django.contrib.auth.models import *
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class user(User):
    timeCreate = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_lenght=250)
    last_name = models.CharField(max_lenght=250)
    cpf = models.CharField(max_lenght=11)
    picture = models.ImageField(upload_to='uploads', verbose_name='Imagem', )
    age = models.CharField(max_lenght=15,verbose_name='Data de Nascimento')
    rate = models.IntegerField(verbose_name='Avaliação', blank=True, null=True)
    balance = models.DecimalField(verbose_name='Saldo', max_digits=100, decimal_places=2)
    telephone = models.CharField(max_lenght=12)
 
    def __str__(self):
        return f'{self.name," ",self.last_name}'

class Motorcycle(models.Model):
    model = models.CharField(max_length=100, verbose_name='Modelo')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    color = models.CharField(max_length=100, verbose_name='Cor')
    year = models.IntegerField(verbose_name='Ano')
    plate = models.CharField(max_lenght=10)
    crlv = models.CharField(max_lenght=20)
    picture_moto = models.ImageField(upload_to='uploads', verbose_name='Imagem')

class Pilot(user): 
    cnh = models.IntegerField()
    status = models.IntegerField()
    motorcycle = models.ManyToManyField(Motorcycle, on_delete=models.CASCADE, verbose_name='Nome')

class Rating(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    text = models.TextField()
    rating = models.IntegerField(verbose_name='Nota', max_digits=10)
    owner = models.ForeignKey(user, verbose_name='Perfil', on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.PROTECT, verbose_name="Cliente")

class Ride(models.Model):
    value = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Valor')
    distance = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Distância')
    pilot = models.ForeignKey(Pilot, on_delete=models.PROTECT,verbose_name="Moto Taxi", null=True)
    client = models.ForeignKey(user, on_delete=models.PROTECT, verbose_name="Cliente")
    start = models.CharField(max_length=300, verbose_name="Começo")
    end = models.CharField(max_length=300, verbose_name="Chegada")
    status = models.BooleanField(default=True)
    timeStart = models.DateTimeField(auto_now_add=True)
    timeEnd = models.DateTimeField()