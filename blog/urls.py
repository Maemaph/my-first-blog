from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register_profile/', views.register, name='register_profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('profile/?P<username>[\w\-]+)/', views.profile, name='profile'),
]
