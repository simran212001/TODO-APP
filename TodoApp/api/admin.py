from django.contrib import admin

from api.models import Task

# Register your models here.
# Register Task model with admin panel
admin.site.register(Task)