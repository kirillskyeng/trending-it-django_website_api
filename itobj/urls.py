from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpage/', addpage, name='add_page'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('categories/', categories, name='categories'),
    path('categories/<int:cat_id>/', show_category, name='show_category'),
    path('post/<int:post_id>/', show_post, name='post'),
]
