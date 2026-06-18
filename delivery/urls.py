from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clients/', views.clients, name='clients'),
    path('ajouter-client/', views.ajouter_client, name='ajouter_client'),
    path('supprimer-client/<int:id>/', views.supprimer_client, name='supprimer_client'),
    path('modifier-client/<int:id>/', views.modifier_client, name='modifier_client'),
    path('commandes/', views.commandes, name='commandes'),
    path('ajouter-commande/', views.ajouter_commande, name='ajouter_commande'),
    path('livraisons/', views.livraisons, name='livraisons'),
    path('ajouter-livraison/', views.ajouter_livraison, name='ajouter_livraison'),
    path('modifier-livraison/<int:id>/', views.modifier_livraison,name='modifier_livraison'),
    path('supprimer-livraison/<int:id>/', views.supprimer_livraison, name='supprimer_livraison'),
]
