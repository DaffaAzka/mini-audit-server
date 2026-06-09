from django.urls import path
from .views import list, create, detail, approve
from audit_teams.views import list as team_list

urlpatterns = [
    path('', list, name='list'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
    path('<int:pk>/approve', approve, name='approve'),
    path('<int:pk>/team', team_list, name="team_list")
]