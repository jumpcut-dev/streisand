# -*- coding: utf-8 -*-

from django_filters import rest_framework as filters

from films.models import Film, Collection, FilmComment, CollectionComment


class FilmFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(
        field_name='description', lookup_expr='icontains')
    genre = filters.CharFilter(field_name='genre_tags')

    class Meta:
        model = Film
        fields = (
            'title',
            'description',
            'genre_tags',
            'year',
        )


class CollectionFilter(filters.FilterSet):
    film_id = filters.NumberFilter(field_name='films__id', lookup_expr='exact')

    class Meta:
        model = Collection
        fields = {
            'id': ['exact', 'in'],
            'films__title': ['iexact', 'istartswith', 'icontains'],
            'creator__username': ['icontains', 'istartswith'],
            'title': ['iexact', 'istartswith'],
        }


class FilmCommentFilter(filters.FilterSet):
    film_id = filters.NumberFilter(field_name='film__id', lookup_expr='exact')
    film_title = filters.CharFilter(field_name='film__title', lookup_expr='icontains')
    body = filters.CharFilter(field_name='text', lookup_expr='icontains')

    class Meta:
        model = FilmComment
        fields = {
            'id': ['exact', 'in'],
            'author__username': ['iexact', 'istartswith'],
        }


class CollectionCommentFilter(filters.FilterSet):
    film_id = filters.NumberFilter(field_name='collection__films__id', lookup_expr='exact')
    film_title = filters.CharFilter(field_name='collection__films__title', lookup_expr='icontains')
    body = filters.CharFilter(field_name='text', lookup_expr='icontains')

    class Meta:
        model = CollectionComment
        fields = {
            'id': ['exact'],
            'collection__id': ['in', 'exact'],
            'author__username': ['iexact', 'istartswith'],
            'collection__creator__username': ['iexact', 'istartswith'],
        }
