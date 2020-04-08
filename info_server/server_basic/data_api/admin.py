from django.contrib import admin
from . import models

# Register your models here.
class ApiAdmin(admin.ModelAdmin):
    list_display = (
        'api_id'
        , 'url'
        , 'text'
        , 'par'
        , 'dev_oper'
        , 'create_time'
        , 'update_time'
    )  # list
    search_fields = (
        'api_id',
        'url',
        'text',
        'par',
    )

admin.site.register(models.api, ApiAdmin)
# admin.site.register(models.api)
