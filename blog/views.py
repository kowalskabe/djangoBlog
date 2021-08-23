from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Basia',
        'title': 'Post Basi',
        'content': 'lorem ipsum',
        'date_posted': '22 August 2021'
    },
    {
        'author': 'Misia',
        'title': 'Post Misi',
        'content': 'lorem ipsum',
        'date_posted': '23 August 2021'
    }

]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
