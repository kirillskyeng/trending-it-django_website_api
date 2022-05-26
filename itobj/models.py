from django.db import models


class ItObject(models.Model):
    title = models.CharField(max_length=80)
    url = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    trending = models.IntegerField(default=0)

    def __str__(self):
        return self.title
