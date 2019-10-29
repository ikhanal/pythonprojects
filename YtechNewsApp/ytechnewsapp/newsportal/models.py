from django.db import models

# Create your models here.

class NewsCategory(models.Model):
    title=models.CharField(max_length=200)
    ordering=models.IntegerField(default=0)
    is_published=models.IntegerField(default=1)
    date_created=models.DateTimeField('date created')
    def __str__(self):
        return self.title
    

class News(models.Model):
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    is_published=models.IntegerField(default=1)
    is_editior_picked=models.IntegerField(default=0) # 1=picked, 0=default'
    searching_tags = models.CharField(max_length=200)
    seo_keywords = models.CharField(max_length=200)
    date_created=models.DateTimeField('date created')
    date_published=models.DateTimeField('date published') 
    def __str__(self):
        return self.title
    
    


   