from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    # if we are using Normal Serializers we need to use create and update methods.
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=1000)
    # date = serializers.DateTimeField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.body = validated_data.get('body', instance.body)
        #instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
