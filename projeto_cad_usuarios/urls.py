
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    

   #rota, view responsavel, nome de referencia 
   path('',views.home,name='home'),
   #era pra ver o usuario, mas aparentemente tenho que mudar o nome 
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]

