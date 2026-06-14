from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required(login_url='/accounts/login/')
def profile(request):
    # Auto-create profile if not exists
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.phone = request.POST.get('phone', '')
        profile.address = request.POST.get('address', '')
        profile.city = request.POST.get('city', '')
        profile.bio = request.POST.get('bio', '')
        profile.save()
        return redirect('/profiles/')

    return render(request, 'profile.html', {'profile': profile})