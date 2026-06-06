from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('groups/', include('groups.urls')),
    path('users/', include('users.urls')),
]