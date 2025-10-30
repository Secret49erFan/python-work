from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

class Blog(models.Model):
    '''A blog the user can post entries to.'''
    blog_name = models.CharField(max_length=30)
    blog_author = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_type = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_name)
        super().save(*args, **kwargs)

    def __str__(self):
        '''Return a string representation of the model.'''
        return self.blog_name
    
class Post(models.Model):
    '''Entries posted to the blog.'''
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''Return a string representation of the entry.'''
        return f'{self.text[:50]}...' if len(self.text) >= 50 else self.text