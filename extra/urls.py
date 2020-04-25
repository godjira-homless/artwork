from django.urls import path
from . import views
from artists import views as artview
from appraisers import views as appview
from technics.views import technic_complete

urlpatterns = [

    path('', views.extra_list, name='extra_list'),
    path('create/', views.create_extra, name='create_extra'),
    path('update/<int:id>', views.update_extra, name='update_extra'),
    path('delete/<int:id>', views.delete_extra, name='delete_extra'),
    # path('<slug:slug>', views.detail_lot, name='detail_lot'),
    path('auto_complete/', artview.auto_complete, name='auto_complete'),
    path('auto_complete_appraiser/', appview.auto_complete_appraiser, name='auto_complete_appraiser'),
    path('technic_complete/', technic_complete, name='technic_complete'),

]

