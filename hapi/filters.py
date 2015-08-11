import django_filters
from hapi.models import Item
from hapi.serializers import ItemSerializer
from rest_framework import generics

class ItemFilter(django_filters.FilterSet):
    #manufacturer = django_filters.CharFilter(name="manufacturer__name")
    category = django_filters.CharFilter(name="category__category")
    class Meta:
        model = Item
        fields = ['category']
