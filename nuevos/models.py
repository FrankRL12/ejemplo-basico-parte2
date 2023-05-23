from django.db import models

# Create your models here.
class Home(models.Model):
    imagen = models.ImageField(upload_to='noticias')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(auto_now_add=True)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='home'
        verbose_name_plural='homes'

    def __str__(self):
        return self.titulo
    

class Noticias(models.Model):
    imagen = models.ImageField(upload_to='recientes')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(auto_now_add=True)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='noticia'
        verbose_name_plural='noticias'

    def __str__(self):
        return self.titulo
    