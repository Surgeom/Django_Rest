from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TODOUser
from .serializator import TODOUserSerializer

# Вот как-то так ,забыл что если сразу запушить все pullrequest не сделать
class TODOUserViewSet(ModelViewSet):
    serializer_class = TODOUserSerializer
    queryset = TODOUser.objects.all()
