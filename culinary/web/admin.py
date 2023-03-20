from django.contrib import admin
from .models import Web, Blog
from django.utils.safestring import mark_safe


class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'text','date')

class WebAdmin(admin.ModelAdmin):
    list_display = ('id','get_image')
    readonly_fields = ("get_image",)

    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    get_image.short_description = 'Изображение'


admin.site.register(Web,WebAdmin)
admin.site.register(Blog, BlogAdmin)
