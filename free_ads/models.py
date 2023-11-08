from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    
class AdPicture(models.Model):
    img_path = models.TextField(max_length=255)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
