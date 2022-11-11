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


class Comments(APIView):
    def get(self, request, board_id, post_id):
        """댓글 전체 조회"""
        pass

    def post(self, request, board_id, post_id):
        """댓글 생성"""
        pass


class CommentsDetail(APIView):
    def get(self, request, board_id, post_id, id):
        """댓글 하나만 조회"""
        pass

    def put(self, request, board_id, post_id, id):
        """댓글 수정"""
        pass

    def delete(self, request, board_id, post_id, id):
        """댓글 삭제"""
        pass
