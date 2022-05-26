from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpage/', addpage, name='add_page'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('cats/', categories),
    path('cats/<int:cat_id>/', categories),
    path('post/<int:post_id>/', show_post, name='post'),
]
