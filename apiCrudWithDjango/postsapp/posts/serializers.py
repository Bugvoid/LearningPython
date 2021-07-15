from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'last_update_on', 'is_active')
