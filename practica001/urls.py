"""practica001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .jwtclaim import JWTClaimsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', include('applications.users.urls')),
    path('account', include('applications.account.urls')),
    path('notes', include('applications.notes.urls')),
    path('events', include('applications.events.urls')),
    path('api/login/',JWTClaimsView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/',TokenRefreshView.as_view(), name="token_refresh")
]
