from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),

    path('panier/', views.panier, name = 'panier'),

    path('commande/', views.commande, name = 'commande'),

]
