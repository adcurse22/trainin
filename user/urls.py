from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ExerciseViewSet, NutritionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'nutrition', NutritionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
