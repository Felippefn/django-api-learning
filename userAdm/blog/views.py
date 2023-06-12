from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, CustomUser
import json
# Create your views here.

def hello1_world(request):
    return HttpResponse("Hello, World! BLOG")


@csrf_exempt
def post_create(request):
    if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     author = request.POST.get('author')
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')
        
        if title and content and author:
            post = Post(title=title, content=content, author=author)
            post.save()
            return JsonResponse({'message': 'Post created successfully'}, status=201)
        else:
            return JsonResponse({'message': 'Invalid data provided'}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@csrf_exempt
def post_list_by_author(request, author_id):
    author = CustomUser.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'post_list.html', {'posts': posts})
