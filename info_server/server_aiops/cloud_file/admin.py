from django.contrib import admin

# Register your models here.
from . import models

class infoAdmin(admin.ModelAdmin):
    list_display = (
        'file_name'
        , 'file_type'
        , 'file_size'
        , 'file_path'
        , 'update_oper'
        , 'update_date'
    )  # list

admin.site.register(models.info, infoAdmin)