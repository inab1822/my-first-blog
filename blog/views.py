from django.shortcuts import render
from django.utils import timezone
from .models import Post # from 다음에있는 마침표(.)는 현재 디렉토리 또는 애플리케이션을 의미


# Create your views here.

def post_list(request): # post_list라는 함수를 만들었다.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})


