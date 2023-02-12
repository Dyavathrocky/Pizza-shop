from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.TextField(null=True , blank=True)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.item_name
