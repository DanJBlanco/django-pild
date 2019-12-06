from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola, primer response de django")

def despedida(request):
    return HttpResponse("Adios")