from rest_framework.serializers import ModelSerializer
from .models import TODOUser


class TODOUserSerializer(ModelSerializer):
    class Meta:
        model = TODOUser
        fields = ['username', 'first_name', 'last_name', 'email']
