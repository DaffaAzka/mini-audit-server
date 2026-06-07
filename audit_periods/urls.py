from django.urls import path
from .views import list, create, detail, approve

urlpatterns = [
    path('', list, name='list'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
    path('<int:pk>/approve', approve, name='approve'),
]