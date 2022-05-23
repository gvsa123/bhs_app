from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('thanks/', views.thanks, name='thanks'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('create_new_customer/', views.create_new_customer, name='create_new_customer'),
    path('search/view_customer_profile/<customer_id>/', views.view_customer_profile, name='view_customer_profile'),
    path('view_customers/view_customer_profile/<customer_id>/', views.view_customer_profile, name='view_customer_profile'),
]