from django.urls import path
from . import views

urlpatterns = [
    path('', views.llista_jugadors, name='llista_jugadors'),
    path('afegir/', views.afegir_jugador, name='afegir_jugador'),
    path('editar/<int:pk>/', views.editar_jugador, name='editar_jugador'),
    path('eliminar/<int:pk>/', views.eliminar_jugador, name='eliminar_jugador'),
]
