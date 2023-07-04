from django.http import JsonResponse, HttpResponse
from .models import Car, Driver
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def hello2_world(request):
    return HttpResponse("Hello, World! CAR")


@csrf_exempt
def car_detail(request, pk):

    owner_obj = Driver.objects.get(pk=pk)

    car_objs = Car.objects.filter(owner_id=owner_obj.id)

    context = {

        "vehicles": car_objs,

        "drivers": owner_obj,

    }

    return render(request, "car_detail.html", context)

@csrf_exempt
def insert_driver(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        license = data.get('license')
        # data = json.loads(request.body)
        # name = request.POST.get('name')
        # license = request.POST.get('license')

        if name and license:
            driver = Driver(name=name, license=license)
            driver.save()
            return JsonResponse({'message': 'Driver created successfully'}, status=201)
        else:
            return JsonResponse({'message': 'Invalid data provided'}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        make = data.get('make')
        model = data.get('model')
        year = data.get('year')
        vin = data.get('vin')
        owner_name = data.get('owner')
        # data = json.loads(request.body)
        # name = request.POST.get('name')
        # license = request.POST.get('license')

        try:
            owner = Driver.objects.get(name=owner_name)
            car = Car(make=make, model=model, year=year, vin=vin, owner=owner)
            car.save()
            return JsonResponse({'message': 'Car added successfully'}, status=201)
        except Driver.DoesNotExist:
                return JsonResponse({'message': 'Invalid owner provided'}, status=400)
        else:
            return JsonResponse({'message': 'Invalid data provided'}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=405)