from django.urls import path
from . import views
from customers import views as custview
from .views import auto_complete_code


urlpatterns = [

    path('', views.sale_list, name='sale_list'),
    path('create_sale/<int:code>', views.create_sale, name='create_sale'),
    # path('create_sale/', views.create_sale, name='create_sale'),
    path('sale_selector/', views.sale_selector, name='sale_selector'),
    # path('update/<int:code>', views.update_lot, name='update_lot'),
    # path('delete/<int:id>', views.delete_extra, name='delete_extra'),
    # path('<slug:slug>', views.detail_lot, name='detail_lot'),
    # path('auto_complete/', artview.auto_complete, name='auto_complete'),
    path('auto_complete_customer/', custview.auto_complete_customer, name='auto_complete_customer'),
    path('auto_complete_code/', auto_complete_code, name='auto_complete_code'),
    # path('auto_complete_appraiser/', appview.auto_complete_appraiser, name='auto_complete_appraiser'),
    # path('technic_complete/', technic_complete, name='technic_complete'),

]

