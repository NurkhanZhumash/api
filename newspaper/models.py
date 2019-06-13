from django.db import models
from django.contrib.auth import get_user_model



class Author(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    avatar = models.ImageField(name='author_image')
    def get_full_name(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()


class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    anons = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='articles')
    name = models.SlugField(max_length=10)
    tag = models.ManyToManyField('Tag',related_name='article')

    def __str__(self):
        return self.title

class Tag(models.Model):
    text = models.SlugField(max_length=25)

    def __str__(self):
        return self.text