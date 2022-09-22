from django.shortcuts import render

# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola mundo xd.</h1>")

def vista2(request):
    return HttpResponse("<h1>Hola denuevo a mi pagina</h1>")