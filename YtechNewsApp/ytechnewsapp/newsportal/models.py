from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number=models.CharField(max_length=20)
    work_phonenumber=models.CharField(max_length=20)
    def __str__(self):
        return self.mobile_number

class Address(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    house_number=models.CharField(max_length=200)
    street_name=models.TextField(max_length=500, blank=False)
    suburb=models.TextField(max_length=200, blank=False)
    state=models.TextField(max_length=200, blank=False)
    post_code=models.IntegerField(blank=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def create_user_address(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_address(sender, instance, **kwargs):
    instance.address.save()




    
    


   