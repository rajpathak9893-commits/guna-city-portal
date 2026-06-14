from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from profiles.models import Profile


def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-id')
    return render(request, 'vehicles.html', {'vehicles': vehicles})


def vehicle_detail(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)

    related_vehicles = Vehicle.objects.filter(
        brand=vehicle.brand
    ).exclude(id=vehicle.id).order_by('-id')[:6]

    context = {
        'vehicle': vehicle,
        'related_vehicles': related_vehicles,
    }
    return render(request, 'detail_vehicles.html', context)


@login_required(login_url='/accounts/login/')
def add_vehicle(request):

    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        Vehicle.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            brand=request.POST.get('brand'),
            model=request.POST.get('model'),
            year=request.POST.get('year'),
            price=request.POST.get('price'),
            location=request.POST.get('location'),
            description=request.POST.get('description'),
            phone=request.POST.get('phone', ''),
            address=request.POST.get('address', ''),
            image=request.FILES.get('image')
        )
        return redirect('vehicle_list')

    return render(request, 'add_vehicle.html', {'profile': profile})