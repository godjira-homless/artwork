from django.urls import path
from artists import views

urlpatterns = [
    path('', views.artists_list, name='artists_list'),
    #path('search/', ArtistResults.as_view(), name='artist_search'),
    # path('<int:id>/', views.artist_detail, name='artist_detail'),
    path('create/', views.create_artist, name='create_artist'),
    path('update_artist/<int:id>', views.update_artist, name='update_artist'),
    path('delete_artist/<int:id>', views.delete_artist, name='delete_artist'),
]