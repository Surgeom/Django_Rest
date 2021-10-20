from django.urls import path
from .views import TODOUserViewSet

app_name = 'userapp'
urlpatterns = [
    path('', TODOUserViewSet.as_view({'get': 'list'})),
]