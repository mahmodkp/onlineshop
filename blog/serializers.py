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
        fields = '__all__'  # ['text', 'created_at']


class VideoGallerySerializer(serializers.ModelSerializer):
    """
    Serializer class for video gallery
    """

    class Meta:
        model = VideoGallery
        fields = '__all__'  # ['text', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for comments
    """
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)

    class Meta:
        model = Comment
        fields = ['user_name', 'text', 'created_at']


class CommentWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for comments
    """
    user_name = serializers.CharField(
        source="user.get_full_name", read_only=True)

    class Meta:
        model = Comment
        fields = ['user_name', 'article', 'text']

    def create(self, validated_data):
        user = self.context['user']
        return Comment.objects.create(user=user, **validated_data)


class ArticleRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer class for writing articles
    """

    category = ArticleCategorySerializer()
    images = ImageGallerySerializer(many=True)
    videos = VideoGallerySerializer(many=True)
    # product_comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields ='__all__'
        # (
        #     "name",
        #     "price",
        #     "quantity",
        #     "description",
        #     "icon",
        #     "is_active",
        #     "category",
        #     'images',
        #     'videos',
        #     # 'product_comments',
        # )

    def create(self, validated_data):
        category = validated_data.pop("category")
        instance, created = Category.objects.get_or_create(**category)
        product = Product.objects.create(**validated_data, category=instance)

        return product

    def update(self, instance, validated_data):
        if "category" in validated_data:
            nested_serializer = self.fields["category"]
            nested_instance = instance.category
            nested_data = validated_data.pop("category")
            nested_serializer.update(nested_instance, nested_data)

        return super(ProductRetrieveSerializer, self).update(instance, validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading products
    """

    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        # [
        #     'category',
        #     'name',
        #     'quantity',
        #     'price',
        #     'description',
        #     'is_active',
        #     'created_at',
        #     'updated_at',
        #     'icon',
        # ]
