from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersView.as_view()),
    path('/signup', views.SignupView.as_view()),
    path("/<pk>", views.UserDetailView.as_view())
]