from django.db import models

# Create your models here.

class itemList(models.Model):
    name = models.CharField( max_length = 50 )
    item_id = models.IntegerField( default = 0 )
    type = models.CharField( max_length = 50 )
    category = models.CharField( max_length = 100 )
    code = models.IntegerField( default = 0 )
    date_from = models.DateTimeField()

    def __unicode__(self):
        return self.code

class products(models.Model):
    name = models.CharField( max_length = 50 )
    product_id = models.IntegerField( default = 0 )
    type = models.CharField( max_length = 50 )
    code = models.IntegerField( default = 0 )
    date_from = models.DateTimeField()

    def __unicode__(self):
        return self.code
