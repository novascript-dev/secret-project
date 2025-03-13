# doctors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:doctor_id>/', views.detalhes_medico, name="detalhes_medico"),  # Lista de médicos
    path('', views.listar_medicos, name="lista_medicos"),
]