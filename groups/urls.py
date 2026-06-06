from django.urls import path
from .views import list, create, detail

urlpatterns = [
    path('', list, name='list'),
    path('create', create, name='create'),
    path('<int:pk>/', detail, name='detail'),
]