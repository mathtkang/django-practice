from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
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


class Posts(APIView):
    def get(self, request):
        """게시글 목록 조회"""
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts, many=True)
        return Response(serializers.data)

    def post(self, request):
        """게시글 생성"""
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            new_post = serializer.save()
            return Response(
                PostSerializer(new_post).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors)


class PostsDetail(APIView):
    def get(self, request, board_id, id):
        """게시글 하나만 조회"""
        return HttpResponse("posts-detail/get")

    def put(self, request, board_id, id):
        """게시글 수정"""
        return HttpResponse("posts-detail/put")

    def delete(self, request, board_id, id):
        """게시글 삭제"""
        return HttpResponse("posts-detail/delete")


class PostsLike(APIView):
    def get(self, request, board_id, id):
        """'좋아요'한 게시글 조회"""
        pass

    def post(self, request, board_id, id):
        """게시글 '좋아요' 누르기"""
        pass
