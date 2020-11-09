from django.contrib import admin

# Register your models here.

from . models import Producto, Genre, Alimento, AlimentoInstance

admin.site.register(Alimento)
admin.site.register(Producto)
admin.site.register(Genre)
admin.site.register(AlimentoInstance)
