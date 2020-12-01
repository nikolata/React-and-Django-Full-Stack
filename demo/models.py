from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(null=True, blank=False, unique=True, max_length=36)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    published = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)