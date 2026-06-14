from django.shortcuts import render,redirect
from .models import School, College, Coaching,Education


def education_home(request):
    schools = School.objects.all()[:6]
    colleges = College.objects.all()[:6]
    coachings = Coaching.objects.all()[:6]

    return render(request, 'education_home.html', {
        'schools': schools,
        'colleges': colleges,
        'coachings': coachings
    })


def schools_list(request):
    schools = School.objects.all()

    return render(request, 'schools.html', {
        'schools': schools
    })


def colleges_list(request):
    colleges = College.objects.all()

    return render(request, 'colleges.html', {
        'colleges': colleges
    })


def coaching_list(request):
    coachings = Coaching.objects.all()

    return render(request, 'coaching.html', {
        'coachings': coachings
    })
# from django.shortcuts import render, redirect
# from .models import Education


def education_list(request):

    educations = Education.objects.all().order_by('-id')

    return render(
        request,
        'education_list.html',
        {'educations': educations}
    )


def add_education(request):

    if request.method == 'POST':

        Education.objects.create(

            name=request.POST.get('name'),

            category=request.POST.get('category'),

            description=request.POST.get('description'),

            location=request.POST.get('location'),

            phone=request.POST.get('phone'),

            email=request.POST.get('email'),

            website=request.POST.get('website'),

            image=request.FILES.get('image')
        )

        return redirect('education_list')

    return render(
        request,
        'add_education.html'
    )