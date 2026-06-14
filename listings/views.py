# businesses/views.py  — sirf add_listing function replace karo

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing, Category, ListingImage


def listings_home(request):
    listings = Listing.objects.filter(status='active').order_by('-is_featured', '-created_at')
    categories = Category.objects.all()

    category_slug = request.GET.get('category')
    if category_slug:
        listings = listings.filter(category__slug=category_slug)

    query = request.GET.get('q')
    if query:
        from django.db.models import Q
        listings = listings.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'listings_home.html', {
        'listings': listings,
        'categories': categories,
        'active_category': category_slug,
        'query': query,
    })


def listing_detail(request, slug):
    listing = get_object_or_404(Listing, slug=slug, status='active')
    listing.views += 1
    listing.save(update_fields=['views'])

    images  = listing.images.all()
    reviews = listing.reviews.select_related('user').all()

    return render(request, 'detail.html', {
        'listing': listing,
        'images': images,
        'reviews': reviews,
    })


@login_required
def add_listing(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        # ── Required fields ──
        title       = request.POST.get('title', '').strip()
        category_id = request.POST.get('category', '').strip()
        description = request.POST.get('description', '').strip()
        phone       = request.POST.get('phone', '').strip()
        address     = request.POST.get('address', '').strip()

        # Server-side validation
        errors = []
        if not title:       errors.append('Business ka naam likhein.')
        if not category_id: errors.append('Category chuniye.')
        if not description: errors.append('Business ki jankari likhein.')
        if not phone:       errors.append('Phone number daalna zaroori hai.')
        if not address:     errors.append('Address daalna zaroori hai.')

        if errors:
            for err in errors:
                messages.error(request, err)
            return render(request, 'add_listing.html', {
                'categories': categories,
                'post_data': request.POST,
            })

        # ── Optional fields (blank is fine) ──
        established_year = request.POST.get('established_year', '').strip() or None

        listing = Listing.objects.create(
            title             = title,
            category_id       = category_id,
            owner             = request.user,
            description       = description,
            phone             = phone,
            whatsapp          = request.POST.get('whatsapp', '').strip(),
            email             = request.POST.get('email', '').strip(),
            website           = request.POST.get('website', '').strip(),
            address           = address,
            area              = request.POST.get('area', '').strip(),
            city              = request.POST.get('city', 'Guna').strip(),
            state             = request.POST.get('state', 'Madhya Pradesh').strip(),
            pincode           = request.POST.get('pincode', '').strip(),
            business_hours    = request.POST.get('business_hours', '').strip(),
            established_year  = established_year,
            gst_number        = request.POST.get('gst_number', '').strip(),
            facebook          = request.POST.get('facebook', '').strip(),
            instagram         = request.POST.get('instagram', '').strip(),
            cover_image       = request.FILES.get('cover_image'),
            status            = 'pending',   # Admin approval required
        )

        # ── Gallery images (optional) ──
        for img in request.FILES.getlist('gallery_images'):
            ListingImage.objects.create(listing=listing, image=img)

        messages.success(
            request,
            f'"{listing.title}" submit ho gaya! Admin approve karne ke baad apni category mein show hoga.'
        )

        # ── Redirect to the listing's category page ──
        # Category ka slug use karke listings_home pe filter ke saath bhejo
        try:
            cat_slug = listing.category.slug
            return redirect(f'/listings/?category={cat_slug}')
        except Exception:
            return redirect('listings_home')

    return render(request, 'add_listing.html', {
        'categories': categories,
    })


@login_required
def edit_listing(request, slug):
    listing    = get_object_or_404(Listing, slug=slug)
    categories = Category.objects.all()

    if listing.owner != request.user:
        messages.error(request, 'Aap is listing ko edit nahi kar sakte.')
        return redirect('listing_detail', slug=slug)

    if request.method == 'POST':
        listing.title            = request.POST.get('title', listing.title).strip()
        listing.category_id      = request.POST.get('category', listing.category_id)
        listing.description      = request.POST.get('description', listing.description).strip()
        listing.phone            = request.POST.get('phone', listing.phone).strip()
        listing.whatsapp         = request.POST.get('whatsapp', listing.whatsapp).strip()
        listing.email            = request.POST.get('email', listing.email).strip()
        listing.website          = request.POST.get('website', listing.website).strip()
        listing.address          = request.POST.get('address', listing.address).strip()
        listing.area             = request.POST.get('area', listing.area).strip()
        listing.city             = request.POST.get('city', listing.city).strip()
        listing.pincode          = request.POST.get('pincode', listing.pincode).strip()
        listing.business_hours   = request.POST.get('business_hours', listing.business_hours).strip()
        listing.facebook         = request.POST.get('facebook', listing.facebook).strip()
        listing.instagram        = request.POST.get('instagram', listing.instagram).strip()
        listing.status           = 'pending'

        if request.FILES.get('cover_image'):
            listing.cover_image = request.FILES['cover_image']

        listing.save()

        for img in request.FILES.getlist('gallery_images'):
            ListingImage.objects.create(listing=listing, image=img)

        messages.success(request, 'Listing update ho gayi! Re-approval pending hai.')
        return redirect('listing_detail', slug=listing.slug)

    return render(request, 'edit_listing.html', {
        'listing': listing,
        'categories': categories,
    })


@login_required
def delete_listing(request, slug):
    listing = get_object_or_404(Listing, slug=slug)

    if listing.owner != request.user:
        messages.error(request, 'Aap is listing ko delete nahi kar sakte.')
        return redirect('listing_detail', slug=slug)

    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Listing delete ho gayi.')
        return redirect('listings_home')

    return render(request, 'confirm_delete.html', {'listing': listing})