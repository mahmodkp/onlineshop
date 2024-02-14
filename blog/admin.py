from django.contrib import admin

# Register your models here.

from blog.models import Article, Category, Comment,ImageGallery,VideoGallery

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ImageGallery)
admin.site.register(VideoGallery)


