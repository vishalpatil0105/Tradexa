from django.urls import path
from .views import index, register, CreatePost


urlpatterns = [
   path('', index, name='index-page'),
   path('register/', register, name='register'),
   path('new/', CreatePost.as_view(), name='new-post'),
]