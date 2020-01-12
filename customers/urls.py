from django.urls import path
from customers import views
from customers.views import SearchResultsView

urlpatterns = [
    path('', views.index, name='customers_list'),
    path('create/', views.create_customer, name='create_customer'),
    path('update/<slug:slug>', views.update_customer, name='update_customer'),
    path('search/', SearchResultsView.as_view(), name='search_results')

]
