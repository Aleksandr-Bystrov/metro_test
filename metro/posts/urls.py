from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:post_id>/', views.PostView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:post_id>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),
    path('<int:post_id>/delete/',
         views.PostDeleteView.as_view(), name='delete_post')
]
