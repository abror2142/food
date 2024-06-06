from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication

from .models import FoodType, Measurement, Ingredient, Food, Comment
from .serializers import FoodTypeSerializer, MeasurementSerializer, IngredientSerializer, FoodSerializer, CommentSerializer


class FoodTypeAPIView(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    authentication_classes = [TokenAuthentication]
    

class MeasurementAPIView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    authentication_classes = [TokenAuthentication]
    
    
class IngredientAPIView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    authentication_classes = [TokenAuthentication]
    
    
class FoodAPIView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    authentication_classes = [TokenAuthentication]
    
    
class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    authentication_classes = [TokenAuthentication]
    