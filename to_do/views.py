from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from to_do.models import Card, Task, User
from to_do.serializer import TaskSerializer


# Create your views here.
class CardAPI(APIView):
    def post(self, request):
        user = request.data["user"]
        email = request.data["email"]
        tasks = request.data["tasks"]
        user = User.objects.get_or_create(name=user)
        card = Card.objects.create(user=user)
        for task in tasks:
            Task.objects.create(card=card, task=task)
        return Response({}, status=status.HTTP_200_OK)

    def get(self, request):
        task_completed = 0
        task_active = 0
        tasks = Task.objects.all().exclude(is_active=False)
        for task in tasks:
            if task.is_completed:
                task_completed += 1
            if task.is_active:
                task_active += 1
        return Response({
            "tasks": TaskSerializer(tasks, many=True).data,
            "tasks completed": task_completed,
            "tasks active": task_active
        }, status=status.HTTP_200_OK)
