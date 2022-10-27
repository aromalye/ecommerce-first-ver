from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search', views.search, name='search'),
]