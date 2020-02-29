from django.urls import path
from . import views
from artists import views as artview

urlpatterns = [

    path('', views.extra_list, name='extra_list'),
    path('create/', views.create_extra, name='create_extra'),
    path('update/<slug:slug>', views.update_extra, name='update_extra'),
    path('delete/<slug:slug>', views.delete_extra, name='delete_extra'),
    # path('<slug:slug>', views.detail_lot, name='detail_lot'),
    path('auto_complete/', artview.auto_complete, name='auto_complete'),

]

