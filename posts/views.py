from django.shortcuts import render
from .models import get_all_posts, show_post
import asyncio



# Create your views here.
def blog(request):
    posts = get_all_posts()

    return render(request, template_name='blog.html', context={'posts': posts})



def my_tools(request):
    return render(request, template_name='my_tools.html')




def about(request):
    return render(request, template_name='about.html')



def post_detail(request, post_slug):
    post_data = show_post(post_slug)

    return render(request, template_name='detail_post.html', context={'post': post_data})