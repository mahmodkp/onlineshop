from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
# Getting the user Model
User = get_user_model()


def get_default_article_category():
    """
    Set deldeted cateory to unknown for an article
    """
    return Category.objects.get_or_create(name="unknown")[0]


def category_image_path(instance, filename):
    """
    Get Image path for category
    """
    return f"blog/category/images/{instance.id}/{filename}"


def article_image_path(instance, filename):
    """
    Get Image path for the article 's icon
    """
    return f"blog/images/{instance.id}/{filename}"


def gallery_image_path(instance, filename):
    """
    Get Image path for the articles
    """
    return f"blog/gallery/images/{instance.id}/{filename}"


def gallery_vodeo_path(instance, filename):
    """
    Get Image Video for the articles
    """
    return f"blog/gallery/videos/{instance.id}/{filename}"


def media_file_path(instance, filename):
    """
    Get file path for media 
    """
    return f"blog/media/{instance.article.id}/{filename}"


class Category(models.Model):
    """
    Category model for saving cateoris in blog
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to=category_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Parent category
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children',
        db_index=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Article model for saving Artticles in blog
    """
    category = models.ForeignKey(
        Category,
        related_name="articles",
        on_delete=models.SET(get_default_article_category),
    )
    title = models.CharField(max_length=200)
    # text = models.TextField(blank=True, null=True)
    text = RichTextUploadingField(blank=True, null=True)
    icon = models.ImageField(
        upload_to=article_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_comments(self):
        """
        Get comments of current article
        """
        return self.comments.filter(is_active=True, is_confirmed=True)

    def get_images(self):
        """
        Get Images of current article
        """
        return self.files.filter(media_type=1, is_active=True)

    def get_videos(self):
        """
        Get Videos of current article
        """
        return self.files.filter(media_type=2, is_active=True)

    def get_audios(self):
        """
        Get Audios of current article
        """
        return self.files.filter(media_type=3, is_active=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class MediaFile(models.Model):
    FILE_CHOICES = (
        (1, 'image'),
        (2, 'video'),
        (3, 'audio'),
    )
    article = models.ForeignKey(
        Article,
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
    Comment Model for saving the comments on articles
    """
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='article_comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.text
