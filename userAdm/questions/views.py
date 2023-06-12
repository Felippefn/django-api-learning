from django.http import JsonResponse, HttpResponse
from .models import Question
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def hello3_world(request):
    return HttpResponse("Hello, World! QUESTIONS")


# Create your views here.
@csrf_exempt
def create_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')

        if question:
            question_text = Question(question_text=question)
            question_text.save()
            return JsonResponse({'message': 'Question created successfully'}, status=201)
        else:
            return JsonResponse({'message': 'Invalid data provided'}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)