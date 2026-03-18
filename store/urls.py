from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories_list, name='categories_list'),
    path('products/', views.products_list, name='products_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('testimonials/', views.testimonials_list, name='testimonials_list'),
    path('contact/', views.contact_submit, name='contact_submit'),
]
