from django import forms

from . models import Blog, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_name', 'blog_author', 'blog_type']
        labels = {'blog_name': 'Name',
                  'blog_author': 'Author',
                  'blog_type': 'Type',}
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Post',}