from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/', categories),
    path('cats/<int:cat_id>/', categories),
]
