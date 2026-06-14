from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from profiles.models import Profile


def jobs_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'job_detail.html', {'job': job})


@login_required(login_url='/accounts/login/')
def add_job(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        logo = request.FILES.get('company_logo')

        Job.objects.create(
            user         = request.user,
            title        = request.POST['title'],
            company      = request.POST['company'],
            location     = request.POST['location'],
            salary       = request.POST['salary'],
            description  = request.POST['description'],
            job_type     = request.POST['job_type'],
            experience   = request.POST.get('experience', ''),
            deadline     = request.POST.get('deadline') or None,
            phone        = request.POST.get('phone', ''),
            whatsapp     = request.POST.get('whatsapp', ''),
            address      = request.POST.get('address', ''),
            company_logo = logo,
            is_approved  =False,  # seedha approved — admin filter nahi
        )
        return redirect('jobs')

    return render(request, 'add_job.html', {'profile': profile})