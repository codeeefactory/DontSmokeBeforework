from django.contrib import admin

from avoidsmoke.models import Comment, Content, Idea
admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Idea)

# Register your models here.
