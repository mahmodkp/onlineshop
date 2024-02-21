from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters
from products.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter

from products.models import (
    Product,
    Category,
    ImageGallery,
    VideoGallery,
    Comment,
)

from .serializers import (
    CommentWriteSerializer,
    ProductCategorySerializer,
    ProductSerializer,
    CommentSerializer,
    ImageGallerySerializer,
    VideoGallerySerializer,
)
from rest_framework.decorators import action
from rest_framework import status


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve product categories
    """

    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (permissions.AllowAny,)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price']

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        instance = self.get_object()
        serializer = ImageGallerySerializer(instance.get_images(), many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get'])
    def videos(self, request, pk=None):
        instance = self.get_object()
        serializer = VideoGallerySerializer(instance.get_videos(), many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, pk=None):
        if self.request.method == 'GET':
            instance = self.get_object()
            serializer = CommentSerializer(instance.get_comments(), many=True)
            return Response(serializer.data)
        elif self.request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                text = serializer.validated_data.get("text")
                product = self.get_object()
                user = self.request.user
                Comment.objects.create(
                    user=user, product=product, text=text)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for Comment
    """
    queryset = Comment.objects.filter(
        is_confirmed=True).order_by(
        '-created_at')  
    serializer_class = CommentWriteSerializer
    http_method_names = ['get', 'post']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'user':self.request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

   

class ImagegalleryViewSet(viewsets.ModelViewSet):
    """
    Viewset for imagegallery
    """
    queryset = ImageGallery.objects.filter(is_active=True)
    serializer_class = ImageGallerySerializer
   

class VideogalleryViewSet(viewsets.ModelViewSet):
    """
    Viewset for videogallery
    """
    queryset = VideoGallery.objects.filter(is_active=True)
    serializer_class = VideoGallerySerializer

