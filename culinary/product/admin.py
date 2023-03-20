from django.contrib import admin
from .models import Product
from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','date','get_image','new_price','old_price' )
    search_fields = ('name',)
    list_editable = ('new_price','old_price')
    list_filter = ('date',)
    readonly_fields = ("get_image",)

    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    get_image.short_description = 'Изображение'

admin.site.register(Product, ProductAdmin)
