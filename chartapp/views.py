from django.shortcuts import render
from .models import Alumno
from json import loads,dumps
# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    context = {
        "alumnos": alumnos
    }
    return render(request, 'chartapp/index.html', context)

def graf(request):
    data = []
    data.append(['Jugador', 'Avance'])
    resultados = Alumno.objects.all() #select * from reto;
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Avance por jugador'
    subtitulo_formato = dumps(subtitulo)
    if len(resultados)>0:
        for registro in resultados:
            nombre = registro.CodAlumno
            avance = registro.avance
            data.append([nombre,avance])
        data_formato = dumps(data) #formatear los datos en string para JSON
        elJSON = {'losDatos':data_formato,'titulo':titulo_formato,'subtitulo':subtitulo_formato}
        return render(request,'pie.html',elJSON)
    else:
        return HttpResponse("<h1> No hay registros a mostrar</h1>")


