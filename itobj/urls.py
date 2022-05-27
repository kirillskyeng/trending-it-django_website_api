from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpost/', addpost, name='add_post'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('categories/', categories, name='categories'),
    path('categories/<slug:cat_slug>/', show_category, name='show_category'),
    path('post/<slug:post_slug>/', show_post, name='post'),
]
