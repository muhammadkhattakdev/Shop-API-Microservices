from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import json


def hello_user(request):

    return JsonResponse({"message":"Hello World"})


def fetch_products(request):

    try:
        products = requests.get('http://product-service:8000/api/products/')
        print(products)
        data = products.json()
        print(data)
        
        return JsonResponse({"status":"success", "data": data})

    except Exception as e:
        print(str(e))
        return JsonResponse({"status":"500", "message":"Internal Server Error"})
