from django.shortcuts import render
from django.http import JsonResponse
from api.models import Category, Product


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(product.to_json())


def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(category.to_json())


def products_by_category(request, category_id):
    products = Product.objects.filter(category=category_id)
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)
