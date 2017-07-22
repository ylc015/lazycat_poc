from django.contrib import admin
from django.models import (
    Restaurant,
    Category,
    OrderItem,
    Order,
    Menu,
)

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'restaurant_name'
        'email',
        'address',
        'city',
        'opening_status',
        'available'
    ]
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'restaurant',
        'description',
        'available'
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'address',
        'city',
        'paid'
    ]

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'product',
        'price', 
        'quantity'
    ]

