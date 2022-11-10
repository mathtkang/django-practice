from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Post,
)
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


class Posts(APIView):
    def get(self, request, board_id):
        """게시글 목록 조회"""
        pass

    def post(self, request, board_id):
        """게시글 생성"""
        pass


class PostsDetail(APIView):
    def get(self, request, board_id, id):
        """게시글 하나만 조회"""
        pass

    def put(self, request, board_id, id):
        """게시글 수정"""
        pass

    def delete(self, request, board_id, id):
        """게시글 삭제"""
        pass


class PostsLike(APIView):
    def get(self, request, board_id, id):
        """'좋아요'한 게시글 조회"""
        pass

    def post(self, request, board_id, id):
        """게시글 '좋아요' 누르기"""
        pass
