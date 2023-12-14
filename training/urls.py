"""
URL configuration for training project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from user.views import CategoryViewSet, ExerciseViewSet, NutritionViewSet,FeedbackCreateView
from .yasp import urlpatterns as doc_urls

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'nutrition', NutritionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
    path('auth/users/', include('djoser.urls')),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),

]

urlpatterns += doc_urls
