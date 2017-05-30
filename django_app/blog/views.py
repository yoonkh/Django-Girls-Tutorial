from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post

User = get_user_model()
from django.utils import timezone

def post_list(request):
    # posts 변수에 ORM을 이용해서 Post의 리스트 ( 쿼리셋 )를 대입
    # post = Post.objects.filter(published_date__lte=timezone.now())
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-created_date')

    context = {
        'title': 'Postlist from post_list view',
        'posts': posts,
    }
    # return HttpResponse('<html><body>Post List</body></html>')
    return render(request, 'blog/post_list.html', context=context)
# Create your views here.


def post_detail(request, pk):
    print('post_detail pk:', pk)
    # post라는 키값으로 Post객체중 pk 또는 id값이 매개변수로 주어진 pk변수와 같은 Post객체를 전달
    # objects.get을 쓰세요
    context = {
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':
        data = request.POST
        title = data['title']
        text = data['text']
        user = User.objects.first()
        post = Post.objects.create(
            title = title,
            text = text,
            author = user
        )
        return redirect('post_detail', pk=post.pk)