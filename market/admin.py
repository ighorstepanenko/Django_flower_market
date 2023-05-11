from django.contrib import admin

from .models import Client, Color, Lot, Order, Comment

class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_seller')
    list_filter = ('is_seller',)
    list_editable = ('is_seller',)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('shade',)
    list_editable = ('shade',)
    list_display_links = None

class LotAdmin(admin.ModelAdmin):
    list_display = ('seller', 'flower_type', 'color', 'quantity', 'price_per_item', 'is_visible')
    list_filter = ('seller',)
    list_editable = ('quantity', 'is_visible')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('lot', 'buyer', 'quantity')
    list_filter = ('lot',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Comment)
admin.site.register(Lot, LotAdmin)
admin.site.register(Order, OrderAdmin)