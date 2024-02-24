from django.contrib import admin

# Register your models here.
from .models import User, Vendor, Product, Vehicle, Checkout

admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Vehicle)
admin.site.register(Checkout)