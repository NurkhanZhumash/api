import django_filters

from .models import Article, Tag


class ArticleFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        to_field_name='name',
        conjoined=True,
    )

    class Meta:
        model = Article
        fields = ['title', 'tags']