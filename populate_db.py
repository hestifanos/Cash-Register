
import os
import django

PRODUCTS = [
    {'upc_code': '123456789012', 'name': 'Product 1', 'price': 10.99},
    {'upc_code': '987654321098', 'name': 'Product 2', 'price': 19.99},
    {'upc_code': '111122223333', 'name': 'Product 3', 'price': 5.99},
]


def populate_products():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cashregister.settings')
    django.setup()

    from sales.models import Product

    for product_data in PRODUCTS:
        upc_code = product_data['upc_code']
        defaults = {
            'name': product_data['name'],
            'price': product_data['price'],
        }
        product, _ = Product.objects.update_or_create(
            upc_code=upc_code,
            defaults=defaults,
        )
        print(product)


if __name__ == '__main__':
    populate_products()
