from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
