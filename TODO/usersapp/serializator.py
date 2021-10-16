from rest_framework.serializers import ModelSerializer
from .models import TODOUser


class TODOUserSerializer(ModelSerializer):
    class Meta:
        model = TODOUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class TODOUserSerializerV2(ModelSerializer):
    class Meta:
        model = TODOUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']
