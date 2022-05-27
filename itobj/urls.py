from django.urls import path
from .views import *

urlpatterns = [
    path('', ItHome.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('categories/<slug:cat_slug>/', ItCategory.as_view(), name='show_category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]
