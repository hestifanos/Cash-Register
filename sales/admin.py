from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('upc_code', 'name', 'price')
    search_fields = ('upc_code', 'name')
    ordering = ('name',)
