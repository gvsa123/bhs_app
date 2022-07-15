from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('thanks/', views.thanks, name='thanks'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('create_new_customer/', views.create_new_customer, name='create_new_customer'),
    path('search/view_customer_profile/<int:customer_id>/', views.view_customer_profile, name='view_customer_profile'),
    path('view_customers/view_customer_profile/<int:customer_id>/', views.view_customer_profile, name='view_customer_profile'),
    path('view_customers/view_customer_profile/<int:customer_id>/create_new_vehicle/', views.create_new_vehicle, name='create_new_vehicle'),
    path('view_customers/view_customer_profile/<int:customer_id>/create_new_comment/', views.create_new_comment, name='create_new_comment'),
    path('view_customers/view_customer_profile/<int:customer_id>/create_new_repair_order/', views.create_new_repair_order, name='create_new_repair_order'),
]