from django.urls import path
from . import views
from artists import views as artview
from customers import views as custview
from appraisers import views as appview
from technics.views import technic_complete

urlpatterns = [

    path('', views.lots_list, name='lots_list'),
    path('create/', views.create_lot, name='create_lot'),
    path('update/<int:code>', views.update_lot, name='update_lot'),
    #path('delete/<int:id>', views.delete_extra, name='delete_extra'),
    # path('<slug:slug>', views.detail_lot, name='detail_lot'),
    path('auto_complete/', artview.auto_complete, name='auto_complete'),
    path('auto_complete_customer/', custview.auto_complete_customer, name='auto_complete_customer'),
    path('auto_complete_appraiser/', appview.auto_complete_appraiser, name='auto_complete_appraiser'),
    path('technic_complete/', technic_complete, name='technic_complete'),

]

