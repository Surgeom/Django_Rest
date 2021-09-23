from rest_framework.serializers import ModelSerializer
from usersapp.serializator import TODOUserSerializer
from .models import UsersProject, TODO


# HyperlinkedModelSerializer как вариант
class UsersProjectSerializer(ModelSerializer):
    td_users = TODOUserSerializer(many=True)


    class Meta:
        model = UsersProject
        fields = '__all__'


class TODOSerializer(ModelSerializer):
    td_user = TODOUserSerializer(many=True)
    todo_project = UsersProjectSerializer()

    class Meta:
        model = TODO
        fields = '__all__'
