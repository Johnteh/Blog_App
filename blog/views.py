from django.shortcuts import render
from .models import Post
posts = [
    {
        'author': 'John miiri',
        'title':'Blog post 1',
        'content': 'First post content',
        'date_posted': 'May 24, 2018'
    },
    {
        'author': 'John miiri',
        'title':'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'May 24, 2018'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 
