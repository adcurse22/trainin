from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Exercise, Nutrition
from .serializers import CategorySerializer, ExerciseSerializer, NutritionSerializer
from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserEditSerializer

class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserEditSerializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()
            return Response({'user': UserEditSerializer(user).data, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
