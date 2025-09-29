from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page to list all available blogs.
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for each blog; including posts.
    path('blogs/<slug:slug>/', views.blog, name='blog'),
    # Page to add a blog.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page to add a post
    path('new_post/<slug:slug>/', views.new_post, name='new_post'),
    # Page to edit a post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]