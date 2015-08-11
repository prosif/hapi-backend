from rest_framework import serializers
from hapi.models import Item,Category 

class ItemSerializer(serializers.HyperlinkedModelSerializer):
   #explicit = serializers.ReadOnlyField()
    category = serializers.SlugRelatedField(read_only=True, slug_field="category")

    class Meta:
        model = Item
        fields = ('url', 'data', 'category', 'explicit')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'category', 'explicit')  
