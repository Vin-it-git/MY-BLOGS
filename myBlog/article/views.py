from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
articles=[
    {
        'id':1,
        'title':'How to write a Blog Post:A Step-by-Step Guide',
        'desc':'Anyone can Connect with their audience through Blogg'
    },
    {
        'id':2,
        'title':'lets go started with an imp',
        'desc':'A blog post is any article'
        
    },
    {
        'id':3,
        'title':'From Geeks to Mainstream',
        'desc':'The world wide web and the idea of a blog...'
        
    },
   
]

def home(request):
    context = {'articles':articles}
    return render(request,'home.html',context)

def blog(request,pk):
    for i in articles:
        if i['id']==pk:
            data = i
            break
    context = {'articles':data}
    return render(request,'blog.html',context)

def about(request):
    return render(request,'about.html')
    
