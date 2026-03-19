import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods

from .models import Category, Product, Testimonial, ContactMessage


def _serialize_category(cat):
    return {
        'id': cat.id,
        'name': cat.name,
        'slug': cat.slug,
        'description': cat.description,
        'icon': cat.icon,
        'image': cat.image.url if cat.image else None,
        'order': cat.order,
        'product_count': cat.products.count(),
    }


def _serialize_product(product):
    return {
        'id': product.id,
        'name': product.name,
        'slug': product.slug,
        'category': {
            'id': product.category.id,
            'name': product.category.name,
            'slug': product.category.slug,
        },
        'description': product.description,
        'price': str(product.price),
        'unit': product.unit,
        'image': product.image.url if product.image else None,
        'is_available': product.is_available,
        'is_featured': product.is_featured,
        'created_at': product.created_at.isoformat(),
    }


def _serialize_testimonial(t):
    return {
        'id': t.id,
        'name': t.name,
        'role': t.role,
        'content': t.content,
        'rating': t.rating,
    }


@require_GET
def home(request):
    featured_products = Product.objects.filter(is_featured=True, is_available=True)[:8]
    categories = Category.objects.all()[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    return JsonResponse({
        'featured_products': [_serialize_product(p) for p in featured_products],
        'categories': [_serialize_category(c) for c in categories],
        'testimonials': [_serialize_testimonial(t) for t in testimonials],
    })


@require_GET
def categories_list(request):
    cats = Category.objects.all()
    return JsonResponse({
        'categories': [_serialize_category(c) for c in cats],
    })


@require_GET
def products_list(request):
    category_slug = request.GET.get('category')
    qs = Product.objects.filter(is_available=True).select_related('category')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        qs = qs.filter(category=category)

    return JsonResponse({
        'products': [_serialize_product(p) for p in qs],
    })


@require_GET
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related = Product.objects.filter(
        category=product.category, is_available=True
    ).exclude(pk=product.pk).select_related('category')[:4]
    return JsonResponse({
        'product': _serialize_product(product),
        'related_products': [_serialize_product(p) for p in related],
    })


@require_GET
def testimonials_list(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    return JsonResponse({
        'testimonials': [_serialize_testimonial(t) for t in testimonials],
    })


@require_http_methods(['POST'])
def contact_submit(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    errors = {}
    if not name:
        errors['name'] = 'Name is required.'
    if not email:
        errors['email'] = 'Email is required.'
    if not subject:
        errors['subject'] = 'Subject is required.'
    if not message:
        errors['message'] = 'Message is required.'

    if errors:
        return JsonResponse({'errors': errors}, status=400)

    ContactMessage.objects.create(
        name=name, email=email, subject=subject, message=message
    )
    return JsonResponse({'message': 'Thank you! Your message has been sent successfully.'}, status=201)
