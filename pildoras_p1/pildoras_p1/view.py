from django.http import HttpResponse, JsonResponse
import datetime
import logging

log = logging.getLogger(__name__)
def saludo(request):
    return HttpResponse("Hola, primer response de django")

def despedida(request):
    return HttpResponse("Adios")

def getDate(request):
    fechaActual = datetime.datetime.now()
    return HttpResponse(fechaActual)

def calculaEdad(request, anio):
    edadActual = 18
    periodo = anio - 2019
    edadFutura = edadActual+periodo
    data = {
        'edadActual': edadActual,
        'periodo': periodo,
        'edadFutura': edadFutura
    }
    log.info("Exit - calculaEdad: ");
    return JsonResponse(data)