from django.contrib import admin
from .models import UsersProject, TODO
from django.forms import CheckboxSelectMultiple
from django.db import models


class ForModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


# Register your models here.
admin.site.register(UsersProject,ForModelAdmin)
admin.site.register(TODO)
