from django.core.validators import MinValueValidator
from django.db import models
from accounts.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField


def get_default_product_category():
    return Category.objects.get_or_create(name="unknown")[0]


def category_image_path(instance, filename):
    """
    Set deleted cateory to unknown for an product
    """
    return f"products/media/category/images/{instance.id}/{filename}"


def product_image_path(instance, filename):
    """
    Get Image path for category
    """
    return f"products/media/product/images/{instance.id}/{filename}"


def gallery_image_path(instance, filename):
    """
    Get Image path for the products 's icon
    """
    return f"products/media/gallery/images/{instance.product.id}/{filename}"


def gallery_vodeo_path(instance, filename):
    """
    Get Image path for the products
    """
    return f"products/media/gallery/videos/{instance.product.id}/{filename}"


def media_file_path(instance, filename):
    """
    Get file path for media
    """
    return f"product/media/{instance.product.id}/{filename}"


class Category(models.Model):
    """
    Category model for saving categoris of products
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to=category_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               related_name='children',
                               db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model for saving Products
    """
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET(get_default_product_category),
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(0)])
    # description = models.TextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    icon = models.ImageField(
        upload_to=product_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def price(self):
    #     return self.prices.filter(is_active=True).last()

    def get_comments(self):
        """Getting comments of a product instance"""
        return Comment.objects.filter(product=self).filter(
            is_active=True).filter(is_confirmed=True)

    def get_images(self):
        """Getting images of a product instance"""
        return self.files.filter(media_type=1, is_active=True)

    def get_videos(self):
        """Getting videos of a product instance"""
        return self.files.filter(media_type=2, is_active=True)

    def get_audios(self):
        """Getting audios of a product instance"""
        return self.files.filter(media_type=3, is_active=True)

    def __str__(self):
        return self.name


# class Price(models.Model):
#     product = models.ForeignKey(
#         Product,
#         related_name="prices",
#         on_delete=models.CASCADE,
#     )
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.price)

#     def __int__(self):
#         return self.price

class MediaFile(models.Model):
    FILE_CHOICES = (
        (1, 'image'),
        (2, 'video'),
        (3, 'audio'),
    )
    product = models.ForeignKey(
        Product,
        related_name='files',
        on_delete=models.CASCADE,
    )
    media = models.FileField(upload_to=media_file_path,
                             null=True)
    media_type = models.IntegerField(
        choices=FILE_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    Comment model for saving Product's comments
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_comments')
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='product_comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.text
