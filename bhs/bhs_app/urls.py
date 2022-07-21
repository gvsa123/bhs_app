from django.urls import path
from . import views
"""
TODO:
- redirect to view_customer_profile after search.
- why did i use underscores? ~ convert to dashes.
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('thanks/', views.thanks, name='thanks'),
    path('view_customers/', views.view_customers, name='view-customers'),
    path('create_new_customer/', views.create_new_customer, name='create-new-customer'),
    path('search/view_customer_profile/<int:customer_id>/', views.view_customer_profile, name='view-customer-profile'),
    path('view_customers/view_customer_profile/<int:customer_id>/', views.view_customer_profile, name='view-customer_profile'),
    path('view_customers/view_customer_profile/<int:customer_id>/view_vehicle_info/<str:vehicle_vin>/', views.view_vehicle_info, name='view-vehicle-info'),
    path('view_customers/view_customer_profile/<int:customer_id>/view_vehicle_info/<str:vehicle_vin>/view_repair_order_info/', views.view_repair_order, name='view-repair-order-info'),
    path('view_customers/view_customer_profile/<int:customer_id>/create_new_vehicle/', views.create_new_vehicle, name='create-new-vehicle'),
    path('view_customers/view_customer_profile/<int:customer_id>/create_new_comment/', views.create_new_comment, name='create-new-comment'),
    path('view_customers/view_customer_profile/<int:customer_id>/create_new_repair_order/', views.create_new_repair_order, name='create-new-repair-order'),
]