from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesView.as_view()),
    path('/<pk>', views.NotesDetail.as_view()),
    path('/<pk>/store', views.NotesStore.as_view()),
    path('/<pk>/text',views.NotesUpdate.as_view())
]