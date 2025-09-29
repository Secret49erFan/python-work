from django.shortcuts import render, get_object_or_404, redirect

from . models import Blog, Post
from . forms import BlogForm, PostForm

def index(request):
    '''The home page for the Blog.'''
    return render(request, 'blogs/index.html')

def blogs(request):
    '''Show a list of the blogs.'''
    blogs = Blog.objects.order_by('-date_added')
    # Use blogs as var in Django template.
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    '''Add a new blog'''
    if request.method != 'POST':
        # No data; create form.
        form = BlogForm()
    else:
        # Data submitted; process blank form.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def new_post(request, slug):
    '''Add a new post to a particular blog.'''
    blog = Blog.objects.get(slug=slug)
    if request.method != 'POST':
        # No data; create blank form.
        form = PostForm()
    else:

        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', slug=slug)
        
    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    blog = post.blog

    if request.method != 'POST':
        # Initial GET request; pre-fill form with current post.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', slug=blog.slug)
    
    # Display a blank or invalid form.
    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)