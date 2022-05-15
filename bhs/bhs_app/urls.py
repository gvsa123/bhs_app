from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('create_new_customer/', views.create_new_customer, name='create_new_customer'),
    path('thanks/', views.thanks, name='thanks'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('search/', views.search, name='search')
]