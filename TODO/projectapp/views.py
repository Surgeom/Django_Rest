from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import UsersProject, TODO
from .serializator import TODOSerializer, UsersProjectSerializer


class UsersProjectViewSet(ModelViewSet):
    serializer_class = UsersProjectSerializer
    queryset = UsersProject.objects.all()


class TODOViewSet(ModelViewSet):
    serializer_class = TODOSerializer
    queryset = TODO.objects.all()
