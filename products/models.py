from django.db import models
from accounts.models import CustomUser
# Create your models here.


def get_default_product_category():
    return Category.objects.get_or_create(name="unknown")[0]


def category_image_path(instance, filename):
    return f"products/media/category/images/{instance.id}/{filename}"


def product_image_path(instance, filename):
    return f"products/media/product/images/{instance.id}/{filename}"


def gallery_image_path(instance, filename):
    return f"products/media/gallery/images/{instance.product.id}/{filename}"


def gallery_vodeo_path(instance, filename):
    return f"products/media/gallery/videos/{instance.product.id}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to=category_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET(get_default_product_category),
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(
        upload_to=product_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def price(self):
    #     return self.prices.filter(is_active=True).last()

    def get_comments(self):
        return Comment.objects.filter(product=self).filter(is_active=True).filter(is_confirmed=True)

    def get_images(self):
        return ImageGallery.objects.filter(product=self).filter(is_active=True)

    def get_videos(self):
        return VideoGallery.objects.filter(product=self).filter(is_active=True)

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
        

class ImageGallery(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=gallery_image_path, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VideoGallery(models.Model):
    product = models.ForeignKey(
        Product, related_name="videos", on_delete=models.CASCADE)
    video = models.FileField(upload_to=gallery_vodeo_path,
                             null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
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
