from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=300)
    description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    day = serializers.DateField()
    from_time = serializers.DateTimeField()
    to_time = serializers.DateTimeField()
    status = serializers.CharField(max_length=1, required=False)


    def create(self, validated_data):
        """
        Create and return a new `Task` instance, given the validated data.
        """
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Task` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.day = validated_data.get('day', instance.day)
        instance.from_time = validated_data.get('from_time', instance.from_time)
        instance.to_time = validated_data.get('to_time', instance.to_time)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
