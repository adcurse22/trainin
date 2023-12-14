from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Exercise, Nutrition
from .serializers import CategorySerializer, ExerciseSerializer, NutritionSerializer
from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class NutritionViewSet(viewsets.ModelViewSet):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializer



class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
