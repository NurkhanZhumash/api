from django.contrib import admin
from .models import Author, Article, Tag

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Tag)