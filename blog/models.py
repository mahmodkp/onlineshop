from django.db import models
from accounts.models import CustomUser
# Create your models here.


def get_default_article_category():
    return Category.objects.get_or_create(name="unknown")[0]


def category_image_path(instance, filename):
    return f"blog/category/images/{instance.name}/{filename}"


def article_image_path(instance, filename):
    return f"blog/images/{instance.name}/{filename}"


def gallery_image_path(instance, filename):
    return f"blog/gallery/images/{instance.name}/{filename}"


def gallery_vodeo_path(instance, filename):
    return f"blog/gallery/videos/{instance.name}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to=category_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="articles",
        on_delete=models.SET(get_default_article_category),
    )
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=article_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_image_path', null=True)
    is_active = models.BooleanField(default=True)


class VideoGallery(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    video = models.FileField(upload_to="gallery_vodeo_path",
                             null=True)
    is_active = models.BooleanField(default=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='article_comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.text
