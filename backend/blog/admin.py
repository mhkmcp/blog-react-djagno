from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'excerpt', 'content', 'author', 'status')
    prepopulated_fields = {'slug': ('title',),}


admin.site.register(Category)
