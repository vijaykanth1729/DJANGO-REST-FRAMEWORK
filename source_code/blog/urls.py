from django.urls import path
from .views import posts_list, post_detail
app_name = 'blog'
urlpatterns = [
    path('posts/', posts_list),
    path('posts/<int:pk>/', post_detail),
]
