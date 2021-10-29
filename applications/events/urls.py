from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventsView.as_view() ),
    path('/<pk>', views.DetailEventsView.as_view())
]