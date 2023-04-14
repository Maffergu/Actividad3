from django.shortcuts import render
from .models import Alumno
# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    context = {
        "alumnos": alumnos
    }
    return render(request, 'chartapp/index.html', context)
