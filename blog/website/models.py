from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(blank=False, max_length=120)
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(default='0')


class Mood(models.Model):
    text = models.TextField(blank=False, max_length=500)
    pub_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(default='0')
