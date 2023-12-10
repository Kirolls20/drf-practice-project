from django.db import models

# Create your models here.

class Product(models.Model):
    title= models.CharField(max_length=255)
    description= models.CharField(max_length=355, blank=True,null=True)
    price = models.DecimalField(max_digits=4,decimal_places=2,default=99.99)

    def __str__(self):
        return f"{self.title}-${self.price}"

    @property
    def get_discount(self):
        return self.price * 0.80
     