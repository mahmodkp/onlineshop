from django.contrib import admin

# Register your models here.

from products.models import (
    MediaFile,
    Product,
    Category,
    Comment,
)


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

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

    inlines = (
        ProductInline,
    )
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


class MediaAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "media_type",
        "is_active",
    ]
    search_fields = ["article"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

    actions = ["make_active", "make_not_active"]

    @admin.action(description="Mark selected media as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected media as not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)


admin.site.register(MediaFile, MediaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)


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
