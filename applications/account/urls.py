from django.urls import path
from . import views

urlpatterns = [
    path('/<pk>/destroy', views.DestroyAccount.as_view())
]