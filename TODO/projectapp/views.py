from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from .models import UsersProject, TODO
from .serializator import TODOSerializer, UsersProjectSerializer
from rest_framework.pagination import LimitOffsetPagination


class Pagination10(LimitOffsetPagination):
    default_limit = 10


class Pagination20(Pagination10):
    default_limit = 20


class UsersProjectViewSet(ModelViewSet):
    serializer_class = UsersProjectSerializer
    queryset = UsersProject.objects.all()
    pagination_class = Pagination10

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = UsersProject.objects.all()
        if name:
            projects = projects.filter(proj_name=name)
        return projects


class TODOViewSet(ModelViewSet):
    serializer_class = TODOSerializer
    queryset = TODO.objects.all()
    pagination_class = Pagination20

    def destroy(self, request, *args, **kwargs):
        todo = get_object_or_404(TODO, pk=kwargs['pk'])
        todo.is_active = False
        todo.save()
        return Response()
