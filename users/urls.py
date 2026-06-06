from django.urls import path
from .views import list, create, detail, assign_user_to_group

urlpatterns = [
    path('', list, name='list'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
    path('assign-group', assign_user_to_group, name='assign_user_to_group'),
]