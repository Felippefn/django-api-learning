from django.http import HttpResponse, JsonResponse
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def hello_world(request):
    return HttpResponse("Hello, World! USERMAIN")


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # email = request.POST.get('email')
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if username and password and email:
            hashed_password = make_password(password)
            user = CustomUser.objects.create_user(username=username, password=hashed_password, email=email)
            user.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)
            print('User created successfully!')
        else:
            return JsonResponse({'message': 'Invalid data provided'}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def show_users(request):
    users_ = CustomUser.objects.all()
    print(users_)
    return render(request, 'user_list.html', {'users': users_})

@csrf_exempt
def user_by_id(request, user_id):
    user_id_response = CustomUser.objects.get(id=user_id)
    print(user_by_id)
    return render(request, 'user_list.html', {'users': user_id_response})
