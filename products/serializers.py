from rest_framework import serializers

from products.models import Product, Category, Comment, ImageGallery, VideoGallery


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for product categories
    """

    class Meta:
        model = Category
        fields = "__all__"


class ProductReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading products
    """

    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for writing products
    """

    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = (
            "name",
            "price",
            "quantity",
            "description",
            "image",
            "is_active",
            "category",
        )

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

        return super(ProductWriteSerializer, self).update(instance, validated_data)


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for comments
    """

    class Meta:
        model = Comment
        fields = ['text', 'created_at']


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
