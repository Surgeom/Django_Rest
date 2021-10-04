from django.shortcuts import render
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import TODOUser
from .serializator import TODOUserSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, get_object_or_404, UpdateAPIView


# class TODOUserViewSet(ModelViewSet):
#     serializer_class = TODOUserSerializer
#     queryset = TODOUser.objects.all()


class TODOUserViewSet(ViewSet, UpdateAPIView):
    # renderer_classes = [JSONRenderer]
    serializer_class = TODOUserSerializer
    queryset = TODOUser.objects.all()

    def list(self, request):
        users = TODOUser.objects.all()
        serializer = TODOUserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(TODOUser, pk=pk)
        serializer = TODOUserSerializer(user)
        return Response(serializer.data)
