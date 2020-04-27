from django.contrib import admin
from . import models

# Register your models here.
class infoAdmin(admin.ModelAdmin):
    list_display = (
        'id'
        , 'group'
        , 'date'
        , 'oper'
        , 'content'
    )  # list
    search_fields = (
        'group'
        , 'date'
        , 'oper'
        , 'content'
    )
    # fields = ('rjxf_id', 'rjxf_type') @

admin.site.register(models.info, infoAdmin)
admin.site.register(models.qq_data_count_bank_other)
admin.site.register(models.qq_data_count_bank_cz)
admin.site.register(models.qq_data_count_bank_big)