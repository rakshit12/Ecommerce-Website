from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    item = Blogpost.objects.all()
    return render(request, 'blog/index.html',{'myposts':item})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html',
                  {'post':post})
