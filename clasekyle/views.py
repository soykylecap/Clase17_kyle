from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo!, hola Kyle!")

def lee_nombre(request, nombre):
    return HttpResponse(f"Mi nombre es {nombre}")

def probando_template(request):

    #abrimos el html
    mi_html = open('./clasekyle/templates/index.html')

    #creamos el template con la clase template
    plantilla = Template(mi_html.read())

    #cerramos el archivo xq ahora quedó cargado en el template
    mi_html.close()

    #creamos un contexto vacio
    mi_contexto = Context()

    #terminamos de construir el template renderizandolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)


