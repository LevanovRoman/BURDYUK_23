from django.contrib import admin
from .models import *
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'photo_big')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    # list_editable = ('is_published',)
    list_filter = ('time_create',)
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')
    list_display_links = ('id', 'name')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created', 'status')
    list_filter = ('status', 'created', 'author')
    search_fields = ('author', 'post', 'text')

admin.site.register(BlogModel, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PriceModel, PriceAdmin)
admin.site.register(FeedbackModel, FeedbackAdmin)
admin.site.register(PortfolioModel, PortfolioAdmin)
admin.site.register(Comment, CommentAdmin)


