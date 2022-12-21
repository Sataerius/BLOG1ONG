from django.shortcuts import render
from blogapp.models import Post
from django.contrib.auth.models import User


def home(request):
    return render(request,'index.html',{})

def lista(request):
    listado_post = Post.objects.all()
    return render(request, 'listado.html', {"listado_post": listado_post})