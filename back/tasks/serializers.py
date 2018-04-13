from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
         if len(value) < 2:
            raise serializers.ValidationError("Title must be longer than 2 characters")

    class Meta:
        model = Task
        fields = ('id','title', 'status')
