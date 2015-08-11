from django.contrib import admin
from hapi.models import Item, Category
from django.contrib.admin import AdminSite

class ItemAdmin(admin.ModelAdmin):
   pass

class CategoryAdmin(admin.ModelAdmin):
   pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
