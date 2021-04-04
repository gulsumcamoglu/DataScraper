from django.db import models




class ProductModel(models.Model):
    name   = models.CharField(max_length=70, blank=False,null=False)
    img    = models.CharField(max_length=70, blank=False,null=False)
    price  = models.FloatField(max_length=100,null=False)

    

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'
        
    
    def __str__(self):
        return self.name

