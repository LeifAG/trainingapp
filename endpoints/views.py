from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity, Workout
from .serializers import ActivitySerializer, WorkoutSerializer
from rest_framework.permissions import IsAuthenticated

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)