from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.show_users, name="show_users"),
    path("<int:user_id>/", views.user_by_id, name="user_by_id")
]