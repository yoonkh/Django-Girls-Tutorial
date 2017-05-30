from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    # posts 변수에 ORM을 이용해서 Post의 리스트 ( 쿼리셋 )를 대입
    post = Post.objects.filter(published_date__lte=timezone.now())


    context = {
        'title': 'Postlist from post_list view',
        'posts': post,
    }
    # return HttpResponse('<html><body>Post List</body></html>')
    return render(request, 'blog/post_list.html', context=context)
# Create your views here.
