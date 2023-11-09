from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('reservation/', views.form_view, name='reservation' ),
    #path('confirmation/', views.confirmation, name='confirmation'),
    path('menu_details/<int:pk>', views.menu_details, name='menu_details'),
    path('kitchen/menu_details/<int:pk>', views.menu_details, name='menu_details'), 
    path('about/', views.about, name="about"),   
]