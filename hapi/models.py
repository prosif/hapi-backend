from django.db import models

class Category(models.Model):
   created = models.DateTimeField(auto_now_add=True)
   category = models.CharField(unique=True, max_length=40, default='')
   approved = models.BooleanField()
   explicit = models.BooleanField(default=False)

   class Meta:
      ordering=('created',)
   
#   def save(self, *args, **kwargs):
#      super(Category, self).save(*args, **kwargs)

   def __unicode__(self):
      return self.category

class Item(models.Model):
   created = models.DateTimeField(auto_now_add=True)
   data = models.CharField(max_length=128, default='')
   category = models.ForeignKey('hapi.Category', related_name='items')
   approved = models.BooleanField()
   explicit = models.BooleanField(default=False)
   
   class Meta:
      ordering=('created',)

   def __unicode__(self):
      return self.data
