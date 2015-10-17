from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .models import Category

def post_list(request): 
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_category(request, category): 
	c=Category.objects.get(name=category)
	posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=c).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})