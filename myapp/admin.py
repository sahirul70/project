from django.contrib import admin
from django.db import models
from .models import Author,Catagory,Journal

# Register your models here.



admin.site.register(Author)
admin.site.register(Catagory)
admin.site.register(Journal)
