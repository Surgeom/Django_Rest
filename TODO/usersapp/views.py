from django.shortcuts import render
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import TODOUser
from .serializator import TODOUserSerializer, TODOUserSerializerV2
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
        if self.request.version == 'v2':
            users = TODOUser.objects.all()
            serializer = TODOUserSerializerV2(users, many=True)
        elif self.request.version == 'v1':
            users = TODOUser.objects.all()
            serializer = TODOUserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if self.request.version == 'v1':
            user = get_object_or_404(TODOUser, pk=pk)
            serializer = TODOUserSerializer(user)
        elif self.request.version == 'v2':
            user = get_object_or_404(TODOUser, pk=pk)
            serializer = TODOUserSerializerV2(user)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return TODOUserSerializerV2
        return TODOUserSerializer
