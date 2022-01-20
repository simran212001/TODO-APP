# We need to tell the REST Framework about our Task model 
# importing serializer from restframework
from rest_framework import serializers
from api.models import Task
# Creating a new class that links the Task with its serializer.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

