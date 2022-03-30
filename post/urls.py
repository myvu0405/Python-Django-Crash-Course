from django.urls import path

from .views import allPosts

urlpatterns = [
    path('', allPosts, name='posts'),
    # path('', PostList.as_view(), name='posts'),
    
]
