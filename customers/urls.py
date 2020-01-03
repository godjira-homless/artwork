from django.urls import path
from customers import views

urlpatterns = [
    path('', views.index, name='customers_list'),
    path('create/', views.create_customer, name='create_customer')

]
