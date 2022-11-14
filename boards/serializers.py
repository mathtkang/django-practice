from rest_framework import serializers
from .models import Board
from posts.models import Post


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = "__all__"
