from django.shortcuts import render
from .models import Home, Noticias

# Create your views here.

def inicio(request):
    home=Home.objects.all()
    return render(request, 'inicio.html', {'homes': home})


def noticia(request):
    noticia=Noticias.objects.all()
    return render(request, 'noticia.html', {'noticias': noticia})
