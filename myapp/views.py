from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
class Home(ListView):
  model = Post
  template_name = "home.html"
  
def detail_blog(request,id):
  blog = get_object_or_404(Post,id=id)
  return render(request, 'blogone.html',{"blog" : blog})


