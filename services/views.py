from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service
from profiles.models import Profile


def services_list(request):
    category = request.GET.get('category', '')
    services = Service.objects.filter(is_approved=True).order_by('-created_at')
    if category:
        services = services.filter(category=category)

    categories = Service.CATEGORY_CHOICES
    return render(request, 'services.html', {
        'services':   services,
        'categories': categories,
        'selected':   category,
    })


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'service_detail.html', {'service': service})


@login_required(login_url='/accounts/login/')
def add_service(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        Service.objects.create(
            user         = request.user,
            name         = request.POST['name'],
            category     = request.POST['category'],
            location     = request.POST['location'],
            price        = request.POST['price'],
            description  = request.POST.get('description', ''),
            experience   = request.POST.get('experience', ''),
            timing       = request.POST.get('timing', ''),
            availability = request.POST.get('availability', ''),
            phone        = request.POST.get('phone', ''),
            whatsapp     = request.POST.get('whatsapp', ''),
            website      = request.POST.get('website', ''),
            photo        = photo,
            is_approved  = False,
        )
        return redirect('services')

    return render(request, 'add_service.html', {'profile': profile})