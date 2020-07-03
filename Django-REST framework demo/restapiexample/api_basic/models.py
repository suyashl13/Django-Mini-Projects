from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
