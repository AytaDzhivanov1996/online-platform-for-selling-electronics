from django.contrib import admin

from mvideo.models import Supplier, Product, Contact


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['level', 'title', 'contact', 'product', 'chain', 'debt', ]
    list_display_links = ['chain']
    list_filter = ['contact__city']
    actions = ['admin_clean']

    @admin.action(description='«admin action», очищающий задолженность перед поставщиком у выбранных объектов.')
    def admin_clean(self, request, queryset):
        queryset.update(debt=None)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'model', 'date', ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'country', 'city', 'street', 'house']
