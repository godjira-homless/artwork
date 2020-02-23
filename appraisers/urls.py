from django.urls import path
from appraisers import views

urlpatterns = [
    path('', views.appraisers_list, name='appraisers_list'),
    path('create/', views.create_appraiser, name='create_appraiser'),
    path('update/<slug:slug>', views.update_appraiser, name='update_appraiser'),
    path('delete/<slug:slug>', views.delete_appraiser, name='delete_appraiser'),

]
