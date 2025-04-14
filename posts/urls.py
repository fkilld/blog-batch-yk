
from django.urls import path
from . import views

urlpatterns = [

    path('create_post/', views.create_post, name='create_post'),
    path('create_tag/', views.create_tag, name='create_tag'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_user_profile/', views.create_user_profile, name='create_user_profile'),
    path('', views.list_posts, name='list_posts'),
    path('list_tags/', views.list_tags, name='list_tags'),
    path('list_users/', views.list_users, name='list_users'),
    path('list_user_profiles/', views.list_user_profiles, name='list_user_profiles'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('update_tag/<int:tag_id>/', views.update_tag, name='update_tag'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('update_user_profile/<int:user_profile_id>/', views.update_user_profile, name='update_user_profile'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete_tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete_user_profile/<int:user_profile_id>/', views.delete_user_profile, name='delete_user_profile'),
    
]

