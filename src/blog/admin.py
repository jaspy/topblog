from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

    readonly_fields = ['author', 'created_at', 'message']


class PostAdmin(admin.ModelAdmin):

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('', {
            'fields': ('title', 'author')
        }),
        ('Date', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
        ('Content', {
            'classes': ('extrapretty'),
            'fields': ('content',)
        }),
    )

    inlines = (CommentInline,)


admin.site.register(Post, PostAdmin)
