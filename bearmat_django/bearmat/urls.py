from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/edit', views.profile_edit, name='profile_edit'),
    path('search/', views.search_detail, name='search_detail'),
    path('search/new', views.search_create, name='search_create'),
    # path('', views.artist_list, name='artist_list'),
    # path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    # path('artists/new', views.artist_create, name='artist_create'),
    # path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    # path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
    # path('songs', views.song_list, name='song_list'),
    # path('songs/<int:pk>', views.song_detail, name='song_detail'),
    # path('songs/new', views.song_create, name='song_create'),
    # path('songs/<int:pk>/edit', views.song_edit, name='song_edit'),
    # path('songs/<int:pk>/delete', views.song_delete, name='song_delete'),
    # path('favorites/<int:song_id>/create', views.add_favorite, name='add_favorite'),
    # path('favorites/<int:song_id>/remove', views.remove_favorite, name='remove_favorite')
]

# Defaults from django.contrib.auth.urls ==>
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
