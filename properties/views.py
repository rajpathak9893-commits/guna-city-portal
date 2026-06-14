from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Property


def property_list(request):

    properties = Property.objects.all().order_by('-id')

    context = {
        'properties': properties
    }

    return render(
        request,
        'property_list.html',
        context
    )


def property_detail(request, id):

    property = get_object_or_404(
        Property,
        id=id
    )

    context = {
        'property': property
    }

    return render(
        request,
        'property_detial.html',
        context
    )


@login_required
def add_property(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        price = request.POST.get('price')

        location = request.POST.get('location')

        description = request.POST.get('description')

        image = request.FILES.get('image')

        Property.objects.create(

            user=request.user,

            title=title,

            price=price,

            location=location,

            description=description,

            image=image

        )

        return redirect('property_list')

    return render(
        request,
        'add_property.html'
    )


@login_required
def delete_property(request, id):

    property = get_object_or_404(

        Property,

        id=id,

        user=request.user

    )

    property.delete()

    return redirect('property_list')