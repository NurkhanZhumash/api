from django.urls import path, include

from .views import ArticleViewSet,AuthorViewSet,TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, base_name='articles')
router.register('authors', AuthorViewSet,base_name='authors')
router.register('tags',TagViewSet,base_name='tags')
urlpatterns = [
    path('',include(router.urls))
]

