from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from boards.models import Board, Like
from . import serializers
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from django.core.paginator import Paginator
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class Posts(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """게시글 목록 조회"""
        all_posts = Post.objects.all()
        serializer = serializers.PostSerializer(all_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """게시글 생성"""
        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            new_post = serializer.save()
            return Response(
                serializers.PostSerializer(new_post).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors)


class PostDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, request, id):
        """게시글 하나만 조회"""
        serializer = serializers.PostSerializer(self.get_object(id))
        return Response(serializer.data)

    def put(self, request, id):
        """게시글 수정"""
        serializer = serializers.PostSerializer(
            self.get_object(id),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_post = serializer.save()
            return Response(serializers.PostSerializer(update_post).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        """게시글 삭제"""
        self.get_object(id).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class PostLike(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        """'좋아요'한 게시글 조회"""
        # all_likes = Like.objects.filter(user=request.user)
        # serializer = serializers.LikeSerializer(
        #     all_likes,
        #     many=True,
        #     context={"request": request},
        # )
        # return Response(serializer.data)
        return HttpResponse("posts-like/get")

    def post(self, request, id):
        """게시글 '좋아요' 누르기"""
        return HttpResponse("posts-like/post")
