from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
# class Category(models.Model):
#     name = models.CharField(max_length=40)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name