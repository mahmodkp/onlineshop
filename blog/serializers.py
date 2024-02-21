from rest_framework import serializers

from blog.models import Article, Category, Comment, ImageGallery, VideoGallery


class ArticleCategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for article categories
    """

    class Meta:
        model = Category
        fields = "__all__"


class ImageGallerySerializer(serializers.ModelSerializer):
    """
    Serializer class for image gallery
    """

    class Meta:
        model = ImageGallery
        fields = '__all__'


class VideoGallerySerializer(serializers.ModelSerializer):
    """
    Serializer class for video gallery
    """

    class Meta:
        model = VideoGallery
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for get comments 
    """
    user_name = serializers.CharField(
        source="user.get_full_name", read_only=True)

    class Meta:
        model = Comment
        fields = ['user_name', 'text', 'created_at']


class CommentWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for create and update comments
    """
    user_name = serializers.CharField(
        source="user.get_full_name", read_only=True)

    class Meta:
        model = Comment
        fields = ['user_name', 'article', 'text']

    def create(self, validated_data):
        user = self.context['user']
        return Comment.objects.create(user=user, **validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading Articles
    """

    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        