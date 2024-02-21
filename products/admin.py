from django.contrib import admin

# Register your models here.

from products.models import (
    Product,
    Category,
    Comment,
    ImageGallery,
    VideoGallery,
)


# Category admin page
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin panel for Category Model
    """
    list_display = [
        "name",
        "description",
        "is_active",
    ]
    search_fields = ["name", "description"]
    ordering = ["name"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

    actions = ["make_active", "make_not_active"]

    @admin.action(description="Mark selected comments as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected comments as not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)

# Product admin page


class ProductAdmin(admin.ModelAdmin):
    """
    Admin panel for Product Model
    """
    list_display = [
        "name",
        "price",
        "quantity",
        # "description",
        "is_active"
    ]
    search_fields = ["name", "description"]
    ordering = ["name"]
    list_filter = ["is_active"]
    list_editable = ["is_active", "quantity"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

    actions = ["make_active", "make_not_active"]

    @admin.action(description="Mark selected products as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected products as not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)


class CommentAdmin(admin.ModelAdmin):
    """
    Admin panel for Comment Model
    """
    list_display = [
        "user",
        "product",
        "text",
        "is_active",
        "is_confirmed",

    ]
    search_fields = ["text"]
    list_filter = ["is_active", "is_confirmed",]
    list_editable = ["is_active", "is_confirmed",]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

    actions = ["make_confirmed", "make_not_confirmed"]

    @admin.action(description="Mark selected comments as confirmed")
    def make_confirmed(self, request, queryset):
        queryset.update(is_confirmed=True)

    @admin.action(description="Mark selected comments as not confirmed")
    def make_not_confirmed(self, request, queryset):
        queryset.update(is_confirmed=False)


class ImageGalleryAdmin(admin.ModelAdmin):
    """
    Admin panel for Imagegallery Model
    """
    list_display = [
        "product",
        "image",
        "is_active",
    ]
    search_fields = ["product"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

    actions = ["make_active", "make_not_active"]

    @admin.action(description="Mark selected comments as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected comments as not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)


class VideoGalleryAdmin(admin.ModelAdmin):
    """
    Admin panel for Videogallery Model
    """
    list_display = [
        "product",
        "video",
        "is_active",
    ]
    search_fields = ["product"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

    actions = ["make_active", "make_not_active"]

    @admin.action(description="Mark selected comments as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected comments as not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ImageGallery, ImageGalleryAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)


# class PriceAdmin(admin.ModelAdmin):
#     list_display = [
#         "price",
#         "created_at",
#         "updated_at",
#         "is_active"
#     ]
#     list_filter = ["is_active"]
#     list_editable = ["is_active"]
#     list_per_page = 30

#     def is_active(self, instance):
#         return instance.is_active()

#     actions = ["make_active", "make_not_active"]

#     @admin.action(description="Mark selected records as active")
#     def make_active(self, request, queryset):
#         queryset.update(is_active=True)

#     @admin.action(description="Mark selected records as not active")
#     def make_not_active(self, request, queryset):
#         queryset.update(is_active=False)


# admin.site.register(Price, PriceAdmin)
