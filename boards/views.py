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
