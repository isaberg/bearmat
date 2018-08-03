from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mission', views.mission, name='mission'),
    path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/edit', views.profile_edit, name='profile_edit'),
    path('profile/<int:pk>/delete', views.profile_delete, name='profile_delete'),
    path('search', views.search_list, name='search_list'),
    path('search/<int:pk>', views.search_detail, name='search_detail'),
    path('search/new', views.search_create, name='search_create'),
    path('search/<int:pk>/edit', views.search_edit, name='search_edit'),
    path('search/<int:pk>/delete', views.search_delete, name='search_delete'),
    path('business/', views.business_list, name='business_list'),
    path('business/<int:pk>', views.business_detail, name='business_detail'),
    path('business/new', views.business_create, name='business_create'),
    path('business/<int:pk>/edit', views.business_edit, name='business_edit'),
    path('business/<int:pk>/delete', views.business_delete, name='business_delete'),


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
