from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jobs.models import Job
from properties.models import Property


@login_required
def dashboard(request):

    jobs = Job.objects.filter(user=request.user)

    properties = Property.objects.filter(user=request.user)

    context = {
        'jobs': jobs,
        'properties': properties
    }

    return render(
        request,
        'dashboard.html',
        context
    )