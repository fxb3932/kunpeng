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