from django.http import JsonResponse
from api.models import Product, Category
import json

def product_list(request):
    # select * from api_product;
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse(products_json, safe=False)

def product_id(request, id):
    products = Product.objects.all()
    product_json = [p.to_json() for p in products]
    for product in product_json:
        if product['id'] == id:
            return JsonResponse(product)
    return JsonResponse({
        "error":"Not Found"
    })

def category_list(request):
    categories = Category.objects.all()
    category_json = [c.to_json() for c in categories]
    return JsonResponse(category_json, safe=False)

def category_id(request, id):
    categories = Category.objects.all()
    category_json = [c.to_json() for c in categories]
    for category in category_json:
        if category['id'] == id:
            return JsonResponse(category)
    return JsonResponse({
        "error":"Not found"
    })   

def product_category(id):
    categories = Category.objects.all()
    category_json = [c.to_json() for c in categories]
    for category in category_json:
        if category['id'] == id:
            return category["name"]

def product_list_with_category(request, id):
    products = Product.objects.all()
    product_json = [p.to_json() for p in products]
    category = product_category(id)
    products_with_category = []
    for product in product_json:
        if product['category'] == category:
            products_with_category.append(product)
    return JsonResponse(products_with_category, safe=False)
        