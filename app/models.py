from sys import version
from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE

# Creat your models here.

class Accesorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=200,blank=False,null=False)
    
    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        db_table = 'accesorio'
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorios'
        ordering = ['id']
    

class Marca(models.Model):
    id= models.AutoField(primary_key=True)  
    nombre= models.CharField(max_length=200,blank=False,null=False) 

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        db_table = 'marca'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']    

class Tipo(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre= models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return f"{self.nombre}"
    
    
    class Meta:
        db_table = 'tipo'
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']  

class Modelo(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre= models.CharField(max_length=200,blank=False,null=False)
    version= models.CharField(max_length=200)       
    ano= models.IntegerField(blank=False,null=False)
    motor= models.CharField(max_length=100,blank=False,null=False)
    transmision= models.CharField(max_length=100,blank=False,null=False)
    frenos= models.CharField(max_length=100,blank=False,null=False)
    medidas= models.CharField(max_length=100)
    tipo= models.ForeignKey(Tipo,on_delete=CASCADE)
    marca= models.ForeignKey(Marca,on_delete=CASCADE)
    accesorio= models.ManyToManyField(Accesorio)

    def __str__(self):
        return f"{self.marca.nombre} {self.nombre} {self.version}"
     
    
    class Meta:
        db_table = 'modelo'
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        ordering = ['id']  

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    modelo= models.ForeignKey(Modelo,on_delete=CASCADE)
    imagen= models.ImageField(upload_to="vehiculos", max_length=200,blank=False,null=False,default="-")
    precio= models.FloatField(blank=False,null=False)
    color= models.CharField(max_length=50,blank=False,null=False)

    # NOMBRE= MODELO.MARCA.TIPO.VERSION
    def __str__(self):
        return f"{self.modelo.marca} {self.modelo.nombre} {self.modelo.version}"
    
    class Meta:
        db_table = 'vehiculo'
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering = ['id']  
    
