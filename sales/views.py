
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

def cash_register(request):
    if request.method == 'POST':
        upc_code = request.POST.get('upc_code')
        product = get_object_or_404(Product, upc_code=upc_code)
        return render(request, 'sales/display_product.html', {'product': product})
    return render(request, 'sales/cash_register.html')



