from django.shortcuts import render
from models import Pages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def barra(request):
	pages = Pages.objects.all()
	respuesta = ""
	for page in pages:
		respuesta += str(page.id) + " : " + page.page + "<br>"
	return HttpResponse(respuesta)

@csrf_exempt
def contenido(request, identificador):
	if request.method == "POST":
		pagina = request.POST['contenido']
		c = Pages(page = pagina)
		c.save()
		identificador = c.id

	if request.method == "PUT":
		pagina = request.body
		c = Pages(page = pagina)
		c.save()
		identificador = c.id

	try:
		c = Pages.objects.get(id = int(identificador)) 
		respuesta = "El contenido es: " + c.page
		

	except Pages.DoesNotExist:
		respuesta = "El contenido no existe. Crealo"
		respuesta += "<form action='' method='POST'>"
		respuesta += "Contenido: <input type='text' name='contenido'>"
		respuesta += "<input type='submit' value='Enviar'>"
		respuesta += "</form>"
		
	return HttpResponse(respuesta)

	
