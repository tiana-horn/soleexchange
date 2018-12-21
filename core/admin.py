from django.contrib import admin
from core.models import User, Shoe, Favorite, Cart

# Register your models here.
class ShoeAdmin(admin.ModelAdmin):
    model = Shoe
    list_display = ("name", "description", "size")

# class CartAdmin(admin.ModelAdmin):
#     model = Cart

admin.site.register(Shoe, ShoeAdmin)
