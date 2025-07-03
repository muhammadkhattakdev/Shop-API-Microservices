from django.shortcuts import render


from django.http import JsonResponse

def product_list(request):
    return JsonResponse({"products": ["Product A", "Product B"]})

