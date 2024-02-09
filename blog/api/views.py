from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (extend_schema, extend_schema_view,
                                   OpenApiParameter, OpenApiExample)

from .serializers import PostSerializer
from posts.models import Post


@extend_schema(tags=["Posts"])
@extend_schema_view(
    get=extend_schema(
        request=PostSerializer,
        responses={
            status.HTTP_200_OK: PostSerializer,
            status.HTTP_400_BAD_REQUEST: None,
        },
        ),
    post=extend_schema(
        request=PostSerializer,
        responses={
            status.HTTP_201_CREATED: PostSerializer,
            status.HTTP_400_BAD_REQUEST: None,
        },
        examples=[
                OpenApiExample(
                    "Пример поста",
                    description="Тестовый пример поста",
                    value=
                    {
                        "title": "testuser",
                        "text": "Some text for post",
                        "author": 1,
                        "is_published": True,
                    },
                    status_codes=[str(status.HTTP_201_CREATED)],
                )]))
class APIPost(APIView):
    """Представление для объектов модели Post."""

    def get(self, request):
        """Получение списка постов."""

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Добавление поста."""

        request.data['author'] = request.user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Posts detail"])
@extend_schema_view(
    get=extend_schema(
        request=PostSerializer,
        responses={
            status.HTTP_200_OK: PostSerializer,
            status.HTTP_404_NOT_FOUND: None,
        },
        ),
    delete=extend_schema(
        request=PostSerializer,
        responses={
            status.HTTP_200_OK: PostSerializer,
            status.HTTP_400_BAD_REQUEST: None,
            status.HTTP_403_FORBIDDEN: None,
            status.HTTP_404_NOT_FOUND: None,
        },
    ),
    put=extend_schema(
        request=PostSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_403_FORBIDDEN: None,
            status.HTTP_404_NOT_FOUND: None,
        },
        examples=[
                OpenApiExample(
                    "Пример поста",
                    description="Тестовый пример поста",
                    value=
                    {
                        "title": "testuser",
                        "text": "Some text for post",
                        "author": 1,
                        "is_published": True,
                    },
                    status_codes=[str(status.HTTP_200_OK)],
                )],
        parameters=[
            OpenApiParameter(
                name='Новый параметр',
                location=OpenApiParameter.QUERY,
                description='Новый параметр для обновления поста',
                required=False,
                type=int
                )]))
class APIPostDetail(APIView):
    """Представление для работы с конкретным объектом Post."""

    def get(self, request, pk):
        """Получение определенного поста."""

        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """Изменение определенного поста."""

        post = get_object_or_404(Post, id=pk)
        if request.user.is_authenticated and post.author == request.user:
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Permission denied"},
                            status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        """Удаление определенного поста."""

        post = get_object_or_404(Post, id=pk)
        if request.user.is_authenticated and post.author == request.user:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Permission denied"},
                            status=status.HTTP_403_FORBIDDEN)
