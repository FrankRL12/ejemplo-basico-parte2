from django.contrib import admin
from .models import Noticias, Home

# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display=('imagen', 'titulo', 'descripcion', 'autor', 'fecha_publicacion')
    readonly_fields=("creado", "actualizado")

admin.site.register(Home, HomeAdmin)



class NoticiaAdmin(admin.ModelAdmin):
    list_display=('imagen', 'titulo', 'descripcion', 'autor', 'fecha_publicacion')
    readonly_fields=("creado", "actualizado")

admin.site.register(Noticias, NoticiaAdmin)
