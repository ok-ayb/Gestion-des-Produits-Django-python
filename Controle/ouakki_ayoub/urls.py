from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searchProduct/', views.search_Product, name='searchProduct'),
    path('commandeParPersonne/', views.commandParPersonne, name='cmdParPersonne'),
    path('detail/<int:id>', views.detail, name='detailP'),
    path('formP/', views.prodF, name='formP'),
    path('formCo/', views.CmdF, name='formCo'),
    path('formCa/', views.CatF, name='formCa'),
]