
import os
import django

# Setting  the DJANGO_SETTINGS_MODULE environment variable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cashregister.settings')

#configuring django's settingns. 
django.setup()

# Importing our models after setting up Django
from sales.models import Product

# Populating the db.
products_data = [
    {'upc_code': '123456789012', 'name': 'Product 1', 'price': 10.99},
    {'upc_code': '987654321098', 'name': 'Product 2', 'price': 19.99},
    {'upc_code': '111122223333', 'name': 'Product 3', 'price': 5.99},
]


for product_data in products_data:
    Product.objects.create(**product_data)

# Displaying product in the db. 
for product in Product.objects.all():
    print(product)
