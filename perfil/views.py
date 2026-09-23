from django.shortcuts import render

# Create your views here.
def perfil_uno(request):
    data={
        "nombre": "Juan", "apellido": "Perez", "edad": 40, "año": 1980
    }
    return render(request, 'perfil/p1.html', data)