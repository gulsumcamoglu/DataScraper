from django.db import models
from autoslug import AutoSlugField




class ProductModel(models.Model):
    name   = models.CharField(max_length=70, blank=False,null=False)
    img    = models.CharField(max_length=70, blank=False,null=False)
    price  = models.CharField(max_length=20,null=False)
    slug = AutoSlugField(populate_from = 'name', unique=True)

    

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'
        
    
    def __str__(self):
        return self.name

