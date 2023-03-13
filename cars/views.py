from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
import datetime
# Create your views here.
def list(request):
    all_cars = models.Cars.objects.all()
    context = {'all_cars':all_cars}
    return render(request, 'cars/list.html', context=context)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        models.Cars.objects.create(brand=brand,year=year)

        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def add_repairs(request):
    if request.POST:
        repair_description = request.POST['repair_description']
        repaired_date = request.POST['repaired_date']
        cars = request.POST['cars']
        print(repair_description)
        print(repaired_date)
        print(cars) 
        models.Repair.objects.create(repair_description=repair_description,repaired_date=repaired_date)
        models.Repair.objects.add(cars=cars)

        return redirect(reverse('cars:add_repairs'))
    else:
        all_cars = models.Cars.objects.all()
        context = {'all_cars':all_cars}
        return render(request, 'cars/add_repairs.html', context=context)

        
def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Cars.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('PK not found!')
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')