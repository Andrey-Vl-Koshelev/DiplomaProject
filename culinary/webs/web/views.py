from django.shortcuts import render, redirect
from .models import Web
from .forms import WebForm
from .models import Blog


def index(request):
    projects = Web.objects.all()
    return render(request, 'web/index.html', {'projects': projects})


def currentweb(request):
    form = WebForm()
    if request.method == 'POST':
        form = WebForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogweb')
    context = {'form': form}
    return render(request, 'web/currentweb.html', context)


def blogweb(request):
    blog = Blog.objects.order_by('-date')
    return render(request, 'web/blogs.html', {'blogs': blog})

def blog(request, pk):
    blogweb_obj = Blog.objects.get(Blog,id=pk)
    return render(request, 'web/blogweb.html', {'blogweb': blogweb_obj})
