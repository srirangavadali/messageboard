from django.db import models

# Create your models here.
class Post(models.Model):
    text=models.TextField()

    def __str__(self):
        return self.text[:70] #this will print the first 70 chars of text field
