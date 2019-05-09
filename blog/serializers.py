from .models import Post, Comment
from rest_framework import serializers

class PostSerializer(serializers.Serializer):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = Comment
        fields = ('author', 'text',)