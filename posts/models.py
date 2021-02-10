from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    
    def __str__(self):  #show the first 50 characters for the text field
        return self.text[:50]

    
