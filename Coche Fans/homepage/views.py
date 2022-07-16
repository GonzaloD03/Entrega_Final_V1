from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from homepage.models import Coche
from homepage.forms import CocheFormulario

# Create your views here.
from .models import Coche

def inicio(request):

      return render(request, "homepage/inicio.html")




def buscador(request):

      return render(request, "homepage/buscador.html")




def login(request):

      return render(request, "homepage/login.html")


def sing_in(request):

      return render(request, "homepage/sing_in.html")



def about(request):

      return render(request, "homepage/about.html")




def añadir(request):

      if request.method == 'POST':

            miFormulario = CocheFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid: 

                  informacion = miFormulario.cleaned_data

                  añadir = añadir (nombre=informacion['nombre'], modelo=informacion['modelo'], asientos=informacion['asientos']) 

                  coche.save()

                  return render(request, "homepage/inicio.html") 

      else: 

            miFormulario= CocheFormulario() 

      return render(request, "homepage/añadir.html", {"miFormulario":miFormulario})




def buscar(request):

      if  request.GET["camada"]:
 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "homepage/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"

      return HttpResponse(respuesta)




def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
      
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)

                return render(request, 'AppStereo/inicio.html', {"mensaje":f"bienvenido {usuario}"})
            else:

                return render(request, "AppStereo/inicio.html", {"mensaje": "usuario o contraseña incorrectos"})
            
        else:

                return render(request, "AppStereo/inicio.html", {"mensaje": "formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppStereo/login.html", {'form': form})   