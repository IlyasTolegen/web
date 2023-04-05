from django.urls import path, re_path
from api import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_id),
    path('categories/', views.category_list),
    path('categories/<int:id>/', views.category_id),
    path('categories/<int:id>/products/', views.product_list_with_category)
]