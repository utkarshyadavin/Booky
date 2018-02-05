from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name



class Info(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title =  models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    link = models.URLField()

    def __str__(self):
         return self.title