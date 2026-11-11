
from django.shortcuts import render
from .models import Product


def cash_register(request):
    if request.method == 'POST':
        upc_code = request.POST.get('upc_code', '').strip()
        if len(upc_code) != 12 or not upc_code.isascii() or not upc_code.isdigit():
            return render(
                request,
                'sales/cash_register.html',
                {
                    'error': 'Enter a 12-digit UPC code.',
                    'upc_code': upc_code,
                },
                status=400,
            )

        try:
            product = Product.objects.get(upc_code=upc_code)
        except Product.DoesNotExist:
            return render(
                request,
                'sales/cash_register.html',
                {
                    'error': 'No product was found for that UPC code.',
                    'upc_code': upc_code,
                },
                status=404,
            )

        return render(request, 'sales/display_product.html', {'product': product})
    return render(request, 'sales/cash_register.html')

