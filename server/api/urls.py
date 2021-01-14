from django.urls import path, include


from . import views

urlpatterns = [
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view())
]