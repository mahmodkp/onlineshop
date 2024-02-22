from rest_framework import serializers

from products.models import (
    MediaFile,
    Product,
    Category,
    Comment,
)


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for product categories
    """

    class Meta:
        model = Category
        fields = "__all__"


class ProductMediaFileSerializer(serializers.ModelSerializer):
    """
    Serializer class for MediaFile model
    """

    class Meta:
        model = MediaFile
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for comments
    """
    user_name = serializers.CharField(source="user", read_only=True)
    read_only_fields = ('created_at',)

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
        fields = ['user_name', 'product', 'text']

    def create(self, validated_data):
        user = self.context['user']
        return Comment.objects.create(user=user, **validated_data)


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading products
    """

    category = serializers.CharField(source="category.name", read_only=True)
    # serializers.Field(source="Price.price")
    price = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'quantity',
            'price',
            'description',
            'is_active',
            'created_at',
            'updated_at',
            'icon',
        ]
