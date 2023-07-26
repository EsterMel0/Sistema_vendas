from django.contrib import admin
from .models import UserAccount, Product, Category, Sale


class UserAdmin(admin.ModelAdmin):
    ...


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    ...


admin.site.register(UserAccount, UserAdmin)
