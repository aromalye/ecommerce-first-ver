from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_order, name='place_order'),
    path('payment', views.payment, name='payment'),
    path('order_completed', views.order_completed, name='order_completed'),

]