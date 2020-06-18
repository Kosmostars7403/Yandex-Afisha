from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('preview',)

    def preview(self, image):
        url = image.get_absolute_image_url()
        return format_html('<img src="{}" height={} />', url, 200)

    fields = ('file', 'preview', 'position')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
