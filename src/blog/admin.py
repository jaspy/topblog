from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


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
        ('Load main image', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
    )

    inlines = (CommentInline,)

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class CommentAdmin(admin.ModelAdmin):
    fields = ('message', 'author', 'post')
       

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
