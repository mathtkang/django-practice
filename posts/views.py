from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from boards.models import Board
from posts.models import Like
from users.models import User
from . import serializers
import json
from django.http import JsonResponse, HttpResponse
from json.decoder import JSONDecodeError
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
)
from django.core.paginator import Paginator
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from django.db.models import Q
import logging


logger = logging.getLogger(__name__)


class Posts(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request):
        """게시글 목록 조회"""
        board_id = request.query_params.get("board_id")
        if board_id is None:
            return HttpResponse(
                'No board_id',
                status=400,
            )
        filter_title = request.query_params.get("title", None)
        filter_content = request.query_params.get("content", None)
        offset = int(request.query_params.get("offset", 0)) # (int) 어디서부터
        count = int(request.query_params.get("count", 10))
        sort_by = request.query_params.get("sort_by")

        # print(filter_title)
        # print(filter_content)
        # print(offset)
        # print(count)


        if not (
            Board.objects
            .filter(id__exact=int(board_id))
            .exists()
        ):
            return HttpResponse('Not found this board id')
        query = (
            Post.objects
            .get_queryset()  # this code is for typing to `QuerySet`
            .filter(board_id__exact=board_id)
        )
        if filter_title is not None:
            query = query.filter(title__contains=filter_title)
        if filter_content is not None:
            query = query.filter(content__contains=filter_content)

        if sort_by is not None:
            sort_by_column, sort_by_order = sort_by.split(".")
            prefix = '-' if sort_by_order == 'desc' else ''
            query = query.order_by(f'{prefix}{sort_by_column}')

        serializer = serializers.PostSerializer(query[offset:count], many=True)

        return Response(serializer.data)


    def post(self, request):
        """게시글 생성"""
        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            new_post = serializer.save()
            return Response(
                {'id': new_post.id},
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
            return Response(
                {'id': update_post.id},
                status=HTTP_200_OK,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        """게시글 삭제"""
        self.get_object(id).delete()
        return Response(status=HTTP_204_NO_CONTENT)

class PostLike(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request: Request, post_id: int):
        """좋아요 누르기"""
        if not (
            Post.objects
            .filter(id__exact=post_id)
            .exists()
        ):
            return JsonResponse({'message': 'Not found post'},  status=HTTP_404_NOT_FOUND)

        if (
            Like.objects
            .filter(
                user_id=request.user.id,
                post_id=post_id,
            )
            .exists()
        ):
            return JsonResponse({'message': 'Already like post'},  status=HTTP_400_BAD_REQUEST)
        
        serializer = serializers.LikeSerializer(
            data={  # type: ignore
                "post_id": post_id,
                "user_id": request.user.id,
            }
        )
        if serializer.is_valid():
            new_like = serializer.save()
            return Response(
                {'id': new_like.id},
                status=HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors)
    
    def delete(self, request: Request, post_id: int):
        """좋아요 취소하기"""
        if (
            Like.objects
            .filter(
                user_id=request.user.id,
                post_id=post_id,
            )
            .exists()
        ):
            Like.objects.get(post_id=post_id).delete()
            return JsonResponse({'message': 'Removed like'}, status=HTTP_204_NO_CONTENT)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

class PostComments(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request, post_id: int):
        """댓글 조회"""
        comments = Comment.objects.filter(post_id__exact=post_id)
        parent_comment_id = request.query_params.get("parent_comment_id")
        if parent_comment_id is not None:
            comments = comments.filter(parent_comment_id__exact=parent_comment_id)

        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request: Request, post_id: int):
        """댓글 생성 & 대댓글 작성"""
        if not (
            Post.objects
            .filter(id__exact=post_id)
            .exists()
        ):
            return JsonResponse({'message': 'Not found post'},  status=HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            new_comment = serializer.save()
            return Response(
                serializers.CommentSerializer(new_comment).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors)


class PostCommentDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, post_id, comment_id):
        try:
            return Comment.objects.get(Q(post_id=post_id) & Q(id=comment_id))
        except Comment.DoesNotExist:
            raise NotFound

    def put(self, request: Request, post_id: int, comment_id: int):
        """댓글 수정"""
        serializer = serializers.CommentSerializer(
            self.get_object(post_id, comment_id),
            data={
                **request.data,
                "post_id": post_id,
                "user_id": request.user.id,
            },
        )
        if serializer.is_valid():
            update_comment = serializer.save()
            return Response(serializers.CommentSerializer(update_comment).data)
        else:
            return Response(serializer.errors)

    def delete(self, request: Request, post_id: int, comment_id: int):
        """댓글 삭제"""
        self.get_object(post_id, comment_id).delete()
        return Response(status=HTTP_204_NO_CONTENT)