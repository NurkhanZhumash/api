
from rest_framework import generics, viewsets
from rest_framework.decorators import detail_route
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ArticleFilter

from .serializers import ArticleSerializer,AuthorSerializer,TagSerializer
from .models import Article,Author,Tag


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backend = (DjangoFilterBackend,)
    filter_fields = ('tag','name')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

