from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('/signin/', views.signin, name='signin'),
    path('/logout', views.signout, name='logout'),
    path('/dashboard', views.dashboard, name='dashboard'),
    path('/my_orders', views.my_orders, name='my_orders'),

    path('/activate/<uidb64>/<token>', views.activate, name='activate')
]