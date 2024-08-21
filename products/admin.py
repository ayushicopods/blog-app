from django.contrib import admin
from .models import Product, Offer


class ProductAdmins(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
# Register your models here


class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OffersAdmin)
admin.site.register(Product,  ProductAdmins)
