from rest_framework import permissions, renderers, viewsets, mixins
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from hapi.models import Item, Category
from hapi.filters import ItemFilter
from rest_framework.permissions import AllowAny
from rest_framework import generics
from hapi.serializers import ItemSerializer, CategorySerializer
import json
from pprint import pprint

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.filter(approved=True)
	serializer_class = ItemSerializer
	http_method_names = ['get', 'head', 'options', 'trace', 'post']
	filter_class = ItemFilter

	def get_queryset(self):	
		return Item.objects.filter(approved=True)	

	def perform_create(self, serializer):
 		to_get = json.load(self.request)
		#print to_get['category']
		#print json.loads(self.request._data)
  		#print self.request.category
		category_id = to_get['category']
                data = to_get['data']
                explicit = False
		category_thing = Category.objects.get(id=category_id)
		serializer.save(approved=False, category=category_thing, data=data, explicit=explicit)
       
class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.filter(approved=True)
	serializer_class = CategorySerializer
	http_method_names = ['get', 'head', 'options', 'trace', 'post']
	filter_backends = (filters.SearchFilter,)
	search_fields = ('category',)

	def get_queryset(self):
		return Category.objects.filter(approved=True)

	def perform_create(self, serializer):
 		to_get = json.load(self.request)
		#print to_get['category']
		#print json.loads(self.request._data)
  		#print self.request.category
		category = to_get['category']
                #data = to_get['data']
                explicit = False
		#category_thing = Category.objects.get(id=category_id)
		serializer.save(approved=False, category=category, explicit=explicit)


	#@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	#def perform_create(self, serializer):
	#		serializer.save(approved=False) 
