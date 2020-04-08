from django.contrib import admin
from . import models

# Register your models here.
class yything(admin.ModelAdmin):
    list_display = (
        'id'
        , 'title'
        , 'reason'
        , 'banknames'
    )  # list
    search_fields = (
        'title',
    )
    # fields = ('rjxf_id', 'rjxf_type') @
admin.site.register(models.yything, yything)
admin.site.register(models.yything_stat)