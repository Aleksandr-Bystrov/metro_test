from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('profile/<str:username>/', views.ProfileView.as_view(),
         name='profile'),
    path('profile_edit/', views.ProfileEditView.as_view(),
         name='edit_profile'),
]
