from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    user_create,
    user_update,
    user_delete
)

urlpatterns = [
    path("", UserListView.as_view(), name='users_list'),
    path("user/create/", user_create, name='user_create'),
    path("user/<slug:slug>/", UserDetailView.as_view(), name='user_detail'),
    path("user/update/<slug:slug>/", user_update, name='user_update'),
    path("user/delete/<int:id>/", user_delete, name='user_delete'),
]