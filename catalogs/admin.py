from django.contrib import admin
from .models import Listing, Category

admin.site.register(Listing)


# Register your models here.

#auto generate  category slug using category name as slug
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)