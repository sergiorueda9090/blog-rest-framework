from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return '{}'.format(self.title)
    
