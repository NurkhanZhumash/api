from rest_framework import serializers
from .models import Article,Author,Tag

class ArticleSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='text'
    )

    class Meta:
        model = Article
        fields = ('__all__')


class AuthorSerializer(serializers.ModelSerializer):
    article = serializers.RelatedField
    class Meta:
        model = Author
        fields = ('id','first_name','last_name','middle_name','author_image','articles')

class TagSerializer(serializers.ModelSerializer):
    article = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Tag
        fields = ('id','text','article')
