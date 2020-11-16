from django.db import models
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    table = models.IntegerField()
    order_time = models.DateTimeField(default = timezone.now)
    content = models.TextField()
    
    def __str__(self):
        return self.content