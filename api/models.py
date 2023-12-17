from django.db import models
import uuid
# Create your models here.

class Menu(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    food_type = models.CharField(max_length=200,blank=False, null=True)
    price = models.IntegerField(blank=False,null=True)

    def __str__(self):
        return self.food_type
    

class Orders(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    food_type = models.CharField(max_length=100,blank=False,null=True)
    table_number = models.CharField(max_length=100,blank=False,null=True)
    quantity = models.IntegerField(blank=False,null=True)
    total = models.IntegerField(blank=False,null=True)

    def __str__(self):
        return self.table_number

