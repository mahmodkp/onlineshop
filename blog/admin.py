from django.contrib import admin

# Register your models here.

from blog.models import (
    Article,
    Category,
    Comment,
    MediaFile,
)


# Category admin page
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "parent",
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


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "title",
        "text",
        "is_active"
    ]
    search_fields = ["title", "text"]
    ordering = ["title"]
    list_filter = ["is_active"]
    list_editable = ["is_active", "is_active"]
    list_per_page = 30

    def is_active(self, instance):
        return instance.is_active()

    actions = ["make_active", "make_not_active"]

    @admin.action(description="Mark selected acticles as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected acticles as not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "article",
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
        "article",
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(MediaFile, MediaAdmin)
