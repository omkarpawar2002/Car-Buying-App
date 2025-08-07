from django.shortcuts import render,redirect
from .forms import CarForm
from django.http import HttpResponse
from .models import Car

# Create your views here.
def buy_car(request):
    form = CarForm()
    if(request.method == 'POST'):
        form = CarForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('show_details')
    template_name = 'car_app/car_form.html'
    context = {'form':form}
    return render(request,template_name,context)

def show_details(request):
    objs = Car.objects.all()
    template_name = 'car_app/show_details.html'
    context = {'records':objs}
    return render(request,template_name,context)

def update_car(request,pk):
    obj = Car.objects.get(id=pk)
    form = CarForm(instance=obj)
    if(request.method == 'POST'):
        form = CarForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('show_details')
    template_name = 'car_app/car_update.html'
    context = {'form':form}
    return render(request,template_name,context)

def delete_car(request,pk):
    obj = Car.objects.get(id=pk)
    form = CarForm()
    if(request.method == 'POST'):
        obj.delete()
        return redirect('show_details')
    template_name = 'car_app/car_delete.html'
    context = {'obj':obj}
    return render(request,template_name,context)
