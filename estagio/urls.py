from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cad_alunos/', views.cad_alunos, name='cad_alunos'),
    path('cad_estagio/', views.cad_estagio, name='cad_estagio'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('detalhes/<int:alu_id>/', views.detalhes, name='detalhes'),
]