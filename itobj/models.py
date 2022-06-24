from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ItObject(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='blog_post')
    trending = models.IntegerField(default=0)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # def increase_views(self):
    #     self.views += 1
    #     self.save()

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'IT Object'
        ordering = ['-time_update']


class Category(models.Model):
    name = models.CharField(max_length=80, db_index=True)
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['id']
