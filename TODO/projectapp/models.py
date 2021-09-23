from django.db import models
from usersapp.models import TODOUser
from django.utils import timezone


class UsersProject(models.Model):
    proj_name = models.CharField(max_length=100)
    repo_url = models.URLField(max_length=200,
                               blank=True,
                               null=True)
    td_users = models.ManyToManyField(TODOUser)


class TODO(models.Model):
    todo_project = models.ForeignKey(UsersProject, on_delete=models.CASCADE)
    todo_text = models.TextField(max_length=600,
                                 blank=True,
                                 null=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    td_user = models.ForeignKey(TODOUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
