from django.shortcuts import render
# Create your views here.
from .models import Project,Resume
from blog.models import Post

def index(request):
    projects = Project.objects.all()
    info = Resume.objects.first()
    blog = Post.objects.all()
    context = {
        'projects': projects,
        'info':info,
        'blog':blog,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request,'contact.html')


def service(request):
    return render(request,'service.html')

def resume(request):
    return render(request,'resume.html')

def projects(request):
    return render(request,'projects.html')


def ListPosts(request):
    return render(request,'listPosts.html')

