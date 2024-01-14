from django.shortcuts import render
import requests

def product_list(request):
    response = requests.get('https://65248470ea560a22a4e9e5cc.mockapi.io/api/v1/product')
    products = response.json()  # Đảm bảo dữ liệu này là một list các dict
    return render(request, 'products/product_list.html', {'products': products})
