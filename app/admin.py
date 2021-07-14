from django.contrib import admin
from .models import Accesorio, Vehiculo, Marca, Tipo, Modelo
# Register your models here.

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_diplsay = '__all__'
    
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_diplsay = '__all__'

@admin.register(Modelo)
class Modelo(admin.ModelAdmin):
    list_diplsay = '__all__'

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_diplsay = '__all__'

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_diplsay = '__all__'