from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from blog.filters import ArticleFilter
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from blog.models import (
    Article,
    Category,
    Comment,
)

from .serializers import (
    BlogCommentWriteSerializer,
    ArticleCategorySerializer,
    ArticleSerializer,
    BlogCommentSerializer,
    BlogMediaFileSerializer,
)
from rest_framework.decorators import action
from rest_framework import status


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve article categories
    """

    queryset = Category.objects.all()
    serializer_class = ArticleCategorySerializer
    permission_classes = (permissions.AllowAny,)


class ArtcleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Get list of all articles and comments and media related to articles
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    search_fields = ['title', 'text', 'category__name']
    ordering_fields = ['created_at']
    filterset_class = ArticleFilter

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(is_active=True)
        return queryset

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        instance = self.get_object()
        serializer = BlogMediaFileSerializer(instance.get_images(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def videos(self, request, pk=None):
        instance = self.get_object()
        serializer = BlogMediaFileSerializer(instance.get_videos(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def audios(self, request, pk=None):
        instance = self.get_object()
        serializer = BlogMediaFileSerializer(instance.get_audios(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, pk=None):
        if self.request.method == 'GET':
            instance = self.get_object()
            serializer = BlogCommentSerializer(instance.get_comments(), many=True)
            return Response(serializer.data)
        elif self.request.method == 'POST':
            serializer = BlogCommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                text = serializer.validated_data.get("text")
                article = self.get_object()
                user = self.request.user
                comments = Comment.objects.create(
                    user=user, article=article, text=text)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for Comment
    """
    queryset = Comment.objects.filter(
        is_confirmed=True).order_by(
        '-created_at')
    serializer_class = BlogCommentWriteSerializer
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={
                                         'user': self.request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# def get_permissions(self):
#         if self.action in ("create", "update", "partial_update", "destroy"):
#             self.permission_classes = (permissions.IsAdminUser,)
#         else:
#             self.permission_classes = (permissions.AllowAny,)
#         return super().get_permissions()
