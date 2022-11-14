from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Board
from . import serializers
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from django.conf import settings
from rest_framework.exceptions import NotFound
from posts.models import Post
from django.http import HttpResponse


class Boards(APIView):
    def get(self, request):
        """게시판 전체 조회"""
        all_boards = Board.objects.all()
        serializer = serializers.BoardSerializer(all_boards, many=True)
        return Response(serializer.data)

    def post(self, request):
        """게시판 생성"""
        serializer = serializers.BoardSerializer(data=request.data)
        if serializer.is_valid():
            new_board = serializer.save()
            return Response(
                serializers.BoardSerializer(new_board).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors)


class BoardDetail(APIView):
    def get_object(self, id):
        try:
            return Board.objects.get(id=id)
        except Board.DoesNotExist:
            raise NotFound

    def get(self, request, id):
        """게시판 하나만 조회"""
        serializer = serializers.BoardSerializer(self.get_object(id))
        return Response(serializer.data)

    def put(self, request, id):
        """게시판 수정"""
        serializer = serializers.BoardSerializer(
            self.get_object(id),
            data=request.data,
            partial=True,  # 부분적업데이트가능
        )
        if serializer.is_valid():
            update_board = serializer.save()
            return Response(serializers.BoardSerializer(update_board).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        """게시판 삭제"""
        self.get_object(id).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Posts(APIView):
    def get_object(self, id):
        try:
            return Post.objects.get(board_id=id)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, request, id):
        """게시글 목록 조회"""
        all_posts = Post.objects.all()
        serializer = serializers.PostSerializer(self.get_object(id), many=True)
        return Response(serializer.data)

    def post(self, request, id):
        """게시글 생성"""
        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            # board_id = request.data.get(Board.id = )
            new_post = serializer.save()
            return Response(
                serializers.PostSerializer(new_post).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors)


class PostDetail(APIView):
    def get(self, request, board_id, post_id):
        """게시글 하나만 조회"""
        return HttpResponse("posts-detail/get")

    def put(self, request, board_id, post_id):
        """게시글 수정"""
        return HttpResponse("posts-detail/put")

    def delete(self, request, board_id, post_id):
        """게시글 삭제"""
        return HttpResponse("posts-detail/delete")
