from django.urls import path
from .views import *

urlpatterns = [
    path('', ItHome.as_view(), name='home'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('categories/<slug:cat_slug>/', ItCategory.as_view(), name='show_category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('like/<slug:post_slug>/', like_view, name='like_post'),
]
