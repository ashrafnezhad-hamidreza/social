from django.contrib import admin
from models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'datetime',
                    'target_type', 'target_id', 'target_object')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text', 'datetime')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
