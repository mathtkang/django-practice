from .models import User
from . import serializers
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
)
from utils.auth import IsAdminUser


class Users(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """본인 정보 조회"""
        user = request.user
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        """본인 프로필 수정"""
        user = request.user
        serializer = serializers.UserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Signup(APIView):
    def post(self, request):
        """회원가입"""
        raw_password = request.data.get("password")
        if not raw_password:
            raise ParseError
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(raw_password)  # hash
            user.save()
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Login(APIView):
    def post(self, request):
        """로그인"""
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            raise ParseError
        user = authenticate(
            request,
            email=email,
            password=password,
        )
        if user:
            login(request, user) # TODO: token Authentication
            return Response({"ok": "Welcome!"})
        else:
            return Response(
                {"error": "wrong password"},
                status=HTTP_400_BAD_REQUEST,
            )


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """로그아웃"""
        logout(request)
        return Response({"ok": "bye!"})


class UserRole(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, id):
        """유저의 role 수정"""
        pass


class ChangePassword(APIView):
    pass

