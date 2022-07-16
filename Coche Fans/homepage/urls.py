from django.urls import path

from homepage import views

urlpatterns = [
  path('', views.inicio, name="Inicio"),
  path('añadir', views.añadir, name="Añadir"),
  path('buscador', views.buscador, name="Buscador"),
  path('login', views.login, name="Login"),
  path('sing_in', views.sing_in, name="Sing In"),
  path('about', views.about, name="About"),
  path('buscar/', views.buscar),
]