"""happy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from hapi.views import ItemViewSet
from hapi import views
from rest_framework.routers import DefaultRouter
from rest_framework.generics import ListCreateAPIView

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
#router.register(r'items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view())
# views.ItemViewSet)
#ListCreateAPIView.as_view(queryset=Item.objects.all(), serializer_class=ItemSerializer), name = 'user-list')
router.register(r'categories', views.CategoryViewSet)
#router.register(r'status', views.StatusViewSet)

urlpatterns = patterns('',
   url(r'^api/', include(router.urls)),
   #url(r'^api/items/$', views.ItemList.as_view()),
   #url(r'^api/items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   url(r'^api/admin/', include(admin.site.urls))
)

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]
