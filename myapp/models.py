from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Catagory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Journal(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    catagory =models.ManyToManyField(Catagory)
    publish_date =models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
