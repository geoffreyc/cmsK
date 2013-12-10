from django.shortcuts import render
from django.http import HttpResponse
from cmsk.blog.models import Post
from django.shortcuts import render, get_object_or_404


# Blog INDEX
def index(request):
    post_list = Post.objects.order_by('-id')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


# Blog VIEW ARTICLE
def read(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/view.html', {'post': post})


# Blog VIEW ARCHIVES
def archives(request):
    return HttpResponse("Viewing archives")
