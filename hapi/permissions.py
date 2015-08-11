from rest_framework import permissions

class IsAdminOrPostOnly(permissions.BasePermission):
   def has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS:
         print request.method
         print "what the fuck"
         return True
      if request.method is 'POST' or 'GET':
         print "what the hell"
         return True
      print "ayy lmao"
      return False
      
