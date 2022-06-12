from django.shortcuts import render
from django.views.generic import ListView   
# Create your views here.
from .models import Post

from django.http import HttpResponseNotFound

def main_page(request):
    posts = Post.objects.all()
    featured = Post.objects.filter(featured="RF")
    return render(request, 'blog/index.html', {
        "posts": posts, 
        "topics": list({i.topic for i in posts}),
        "count":4,
        "bigpost":Post.objects.filter(featured="LF")[0],
        "featured":sorted(featured,key=lambda x:x.feature_index)
        })



def blog_post(request,slug):
    posts = Post.objects.filter(slug=slug)
    if len(posts):
        post = posts[0]
        return render(request,'blog/blog_post.html',{
            "post":post,
            "topic":post.topic,
            "posts":Post.objects.filter(topic=post.topic).exclude(slug=slug)
        })
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


def topic_page(request,topic):
    if topic in list({i.topic for i in Post.objects.all()}):
        return render(request,'blog/topic-page.html',{
            "topic":topic,
            "posts":Post.objects.filter(topic=topic),
        })
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def error_404(request,exception):
    return render(request,'blog/error-404.html')