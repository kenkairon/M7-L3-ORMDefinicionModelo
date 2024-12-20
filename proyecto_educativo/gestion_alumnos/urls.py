from django.urls import path 
from . import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('estudiantes',views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiante/nuevo/',views.crear_estudiante, name='crear_estudiantes'),
]