from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'due_date')

        # TODO change the serialization to comply with the OpenAPI Specification: 
        # - https://swagger.io/specification/
        # - https://dev.to/errietta/documenting-a-django-api-with-openapi-and-dataclasses-1p6h
