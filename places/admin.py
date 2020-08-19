from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('preview',)
    extra = 0

    def preview(self, image):
        url = image.file.url
        return format_html('<img src="{}" height={} />', url, 200)

    fields = ('position', 'file', 'preview')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
