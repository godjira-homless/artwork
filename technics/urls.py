from django.urls import path
from technics import views
from technics.views import SearchResultsView

urlpatterns = [
    path('', views.technics_list, name='technics_list'),
    path('create/', views.create_technic, name='create_technic'),
    path('update/<slug:slug>', views.update_technic, name='update_technic'),
    path('search/', SearchResultsView.as_view(), name='search_results')

]
