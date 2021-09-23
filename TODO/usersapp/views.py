from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TODOUser
from .serializator import TODOUserSerializer

# случайно сразу в мейн все запушил
class TODOUserViewSet(ModelViewSet):
    serializer_class = TODOUserSerializer
    queryset = TODOUser.objects.all()
