import graphene
from graphene_django import DjangoObjectType
from usersapp.models import TODOUser
from projectapp.models import UsersProject, TODO


class UsersG(DjangoObjectType):
    class Meta:
        model = TODOUser
        fields = '__all__'


class TODOG(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class UsersProjectG(DjangoObjectType):
    class Meta:
        model = UsersProject
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UsersG)
    all_todo = graphene.List(TODOG)
    all_proj = graphene.List(UsersProjectG)

    def resolve_all_users(root, info):
        return TODOUser.objects.all()

    def resolve_all_todo(root, info):
        return TODO.objects.all()

    def resolve_all_proj(root, info):
        return UsersProject.objects.all()


schema = graphene.Schema(query=Query)
