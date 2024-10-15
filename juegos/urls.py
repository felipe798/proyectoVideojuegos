from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideojuegoList.as_view(), name='videojuego-list'),
    path('generos/', views.GeneroList.as_view(), name='genero-list'),
    path('generos/<int:pk>/', views.GeneroDetail.as_view(), name='genero-detail'),
    path('videojuegos/', views.VideojuegoList.as_view(), name='videojuego-list'),
    path('videojuegos/<int:pk>/', views.VideojuegoDetail.as_view(), name='videojuego-detail'),
]
