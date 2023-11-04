from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

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

